from django.db import models
from django.conf import settings

PAYMENT_TYPES= [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта'),
        ('transfer', 'Банковский перевод'),
        ('online', 'Онлайн оплата'),
        ('crypto', 'Криптовалюта'),
    ]

OPERATION_TYPE_CHOICES = [
    ('new_client', 'Новый клиент'),
    ('rename', 'Переименовать клиента'),
    ('add_adress', 'Добавить адресс'),
    ('payment_change', 'Изменения формы оплаты')

    ]


STATUS_CHOICES = [
        ('new', 'Новый'),
        ('confirm', 'Подтвержден'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]



class Application(models.Model):
    operations_type = models.CharField(
        max_length=255,
        choices=OPERATION_TYPE_CHOICES,
        default=OPERATION_TYPE_CHOICES[0][0],
    )
    payment_type = models.CharField(
        max_length=255,
        choices=PAYMENT_TYPES,
        default=PAYMENT_TYPES[0][0]
    )

    status = models.CharField(choices=STATUS_CHOICES, default='new', verbose_name='Status')
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