import re

# Константы вынесены наверх файла
CITY_MARKERS = [
    "г ", "г.", "город",
    "поселок", "пгт",
    "село", "с ",
    "деревня", "д "
]

STREET_MARKERS = [
    "ул ", "ул.", "улица",
    "пр ", "пр.", "проспект",
    "пер ", "пер.", "переулок",
    "б-р", "бульвар",
    "наб", "набережная",
    "ш ", "ш.", "шоссе",
    "пл ", "пл.", "площадь",
]

HOUSE_PATTERNS = [
    r"д\.?\s*(\d+[а-яА-Я]?/?\d*[а-яА-Я]?)",
    r"дом\s*(\d+[а-яА-Я]?/?\d*[а-яА-Я]?)",
    r",\s*(\d+[а-яА-Я]?/?\d*[а-яА-Я]?)\s*[,.]?$",
    r"(\d+[а-яА-Я]?/?\d*[а-яА-Я]?)\s*$",
]


def make_result(valid, message, parts=None):
    """Единый формат результата проверки."""
    return {
        "is_valid": valid,
        "message": message,
        "parts": parts or {}
    }


def validate_address_format(address):
    """
    Проверка структуры адреса.

    Проверяет наличие:
    - населённого пункта
    - улицы
    - номера дома
    """

    if not address or not address.strip():
        return make_result(False, "Адрес не заполнен")

    address = address.strip()
    address_lower = address.lower()

    has_city = any(marker in address_lower for marker in CITY_MARKERS)
    has_street = any(marker in address_lower for marker in STREET_MARKERS)

    has_house = False
    house_number = None

    for pattern in HOUSE_PATTERNS:
        match = re.search(pattern, address)
        if match:
            has_house = True
            house_number = match.group(1)
            break

    parts = {
        "has_city": has_city,
        "has_street": has_street,
        "has_house": has_house,
        "house_number": house_number,
    }

    if has_city and has_street and has_house:
        return make_result(
            True,
            "Адрес содержит город, улицу и номер дома.",
            parts,
        )

    missing = []

    if not has_city:
        missing.append("город")

    if not has_street:
        missing.append("улицу")

    if not has_house:
        missing.append("номер дома")

    return make_result(
        False,
        f"Не найдено: {', '.join(missing)}",
        parts,
    )


def check_application_address(application):
    """
    Проверяет все адреса заявки.

    Возвращает:
        True  - если все адреса корректны.
        False - если найдено хотя бы одно замечание.
    """

    legal_result = validate_address_format(application.legal_address)
    actual_result = validate_address_format(application.actual_address)
    delivery_result = validate_address_format(application.delivery_address)

    all_valid = all([
        legal_result["is_valid"],
        actual_result["is_valid"],
        delivery_result["is_valid"],
    ])

    if all_valid:

        application.address_check_status = "passed"
        application.address_check_message = (
            "Все адреса содержат город, улицу и номер дома."
        )

    else:

        errors = []

        if not legal_result["is_valid"]:
            errors.append(f"Юридический адрес: {legal_result['message']}")

        if not actual_result["is_valid"]:
            errors.append(f"Фактический адрес: {actual_result['message']}")

        if not delivery_result["is_valid"]:
            errors.append(f"Адрес доставки: {delivery_result['message']}")

        application.address_check_status = "failed"
        application.address_check_message = "; ".join(errors)

    application.save()

    return all_valid