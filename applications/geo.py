from django.utils import timezone


def check_application_gps(application):
    """
    Проверяет корректность GPS-координат заявки.

    Формат:
        55.7558,37.6176
        55.7558, 37.6176
        55.7558 ; 37.6176

    Возвращает:
        True  - координаты корректны
        False - координаты некорректны
    """

    gps = application.gps_coordinates

    def fail(message):
        application.geo_check_status = "failed"
        application.geo_check_message = message
        application.geo_checked_at = timezone.now()
        application.save()
        return False

    if not gps or not gps.strip():
        return fail("GPS координаты не заполнены")

    try:
        cleaned = gps.replace(";", ",")
        parts = [part.strip() for part in cleaned.split(",") if part.strip()]

        if len(parts) != 2:
            return fail(
                f"Ожидается 2 координаты, получено {len(parts)}"
            )

        lat = float(parts[0])
        lon = float(parts[1])

        if not (-90 <= lat <= 90):
            return fail(f"Широта {lat} вне диапазона (-90...90)")

        if not (-180 <= lon <= 180):
            return fail(f"Долгота {lon} вне диапазона (-180...180)")

        application.geo_check_status = "passed"
        application.geo_check_message = "GPS координаты корректны"
        application.geo_checked_at = timezone.now()
        application.save()

        return True

    except ValueError:
        return fail("GPS координаты должны содержать два числа")

    except Exception as e:
        return fail(f"Ошибка проверки GPS: {e}")