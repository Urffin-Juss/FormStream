from django.db import models



OPERATION_TYPE_CHOICES = [
    ("new_client", "Новый клиент"),
    ("rename_client", "Переименование клиента"),
    ("add_address", "Добавить адрес существующему клиенту"),
    ("change_payment", "Изменение формы оплаты"),
]

PAYMENT_TYPE_CHOICES = [
    ("fact", "Факт"),
    ("cashless", "Безналичная оплата"),
    ("delivery_to_delivery", "От поставки до поставки"),
    ("prepayment", "Предоплата"),
]

STATUS_CHOICES = [
    ("new", "Новая"),
    ("needs_review", "Требует проверки"),
    ("approved", "Проверена"),
    ("exported", "Выгружена"),
    ("rejected", "Отклонена"),
]



class Application(models.Model):
    operation_type = models.CharField(
        max_length=255,
        choices=OPERATION_TYPE_CHOICES,
        default=OPERATION_TYPE_CHOICES[0][0],
    )
    payment_type = models.CharField(
        max_length=255,
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYMENT_TYPE_CHOICES[0][0]
    )

    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default="new",
        verbose_name="Статус",
    )
    client_name = models.TextField(
        max_length=255,
    )
    inn = models.CharField(max_length=255, blank=False, null=False)
    kpp = models.CharField(max_length=255, blank=False, null=False)
    legal_address = models.TextField(max_length=255, blank=False, null=False)
    actual_address = models.TextField(max_length=255, blank=False, null=False)
    delivery_address = models.TextField(max_length=255, blank=False, null=False)
    gps_coordinates = models.CharField(blank=False, null=False)
    contact_person = models.TextField(max_length=255, blank=False, null=False)
    contact_phone = models.CharField(blank=False, null=False, max_length=255)
    delivery_start_time = models.TimeField(blank=False, null=False)
    delivery_end_time = models.TimeField(blank=False, null=False)
    break_start_time = models.TimeField(blank=True, null=True)
    break_end_time = models.TimeField(blank=True, null=True)