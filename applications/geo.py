from applications.models import Application


def check_application_gps(application):
    """
    Проверяет валидность GPS координат в заявке.
    Возвращает True, если координаты корректны, иначе False.
    """
    gps = application.gps_coordinates


    if not gps or not gps.strip():
        application.geo_check_status = "failed"
        application.geo_check_message = "GPS координаты не заполнены"
        application.save()
        return False

    try:

        cleaned = gps.replace(';', ',').replace('  ', ' ')
        parts = [p.strip() for p in cleaned.split(',') if p.strip()]

        if len(parts) != 2:
            application.geo_check_status = "failed"
            application.geo_check_message = f"Ожидается 2 координаты, получено {len(parts)}"
            application.save()
            return False


        try:
            lat = float(parts[0])
            lon = float(parts[1])
        except ValueError as e:
            application.geo_check_status = "failed"
            application.geo_check_message = f"Неверный формат координат: {e}"
            application.save()
            return False


        if -90 <= lat <= 90 and -180 <= lon <= 180:
            application.geo_check_status = "passed"
            application.geo_check_message = "GPS координаты корректны"
            application.save()
            return True
        else:
            application.geo_check_status = "failed"
            application.geo_check_message = f"Координаты вне допустимого диапазона: широта {lat} (должна быть -90..90), долгота {lon} (должна быть -180..180)"
            application.save()
            return False

    except Exception as e:

        application.geo_check_status = "failed"
        application.geo_check_message = f"Ошибка при проверке координат: {str(e)}"
        application.save()
        return False