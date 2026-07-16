from .geo import check_application_gps
from .adresses import check_application_address


def validate_application(application):
    """
    Выполняет все автоматические проверки заявки.
    """

    check_application_gps(application)
    check_application_address(application)

