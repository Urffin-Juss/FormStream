from django.db import models
from django.conf import settings

PAYMENT_TYPE_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта'),
        ('transfer', 'Банковский перевод'),
        ('online', 'Онлайн оплата'),
        ('crypto', 'Криптовалюта'),
    ]

OPERATOR_CHOICES = [
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
        choices=settings.OPERATIONS_CHOICES,
        default=settings.OPERATIONS_CHOICES[0][0],
    )
    payment_type = models.CharField(
        max_length=255,
        choices=settings.PAYMENT_TYPES,
        default=settings.PAYMENT_TYPES[0][0]
    )

    status = models.CharField(choices=STATUS_CHOICES, default='new', verbose_name='Status')
    client_name = models.TextField(
        max_length=255,
    )
    inn = models.IntegerField(max_length=12, blank=False, null=False)
    kpp = models.CharField(max_length=255, blank=False, null=False)
    legal_address = models.TextField(max_length=255, blank=False, null=False)
    actual_address = models.TextField(max_length=255, blank=False, null=False)
    delivery_address = models.TextField(max_length=255, blank=False, null=False)
    gps_coordinates = models.IntegerField(blank=False, null=False)
    contact_person = models.TextField(max_length=255, blank=False, null=False)
    contact_phone = models.IntegerField(blank=False, null=False, max_length=11)
    delivery_start_time = models.DateTimeField(blank=False, null=False)
    delivery_end_time = models.DateTimeField(blank=False, null=False)
    break_start_time = models.DateTimeField(blank=False, null=False)
    break_end_time = models.DateTimeField(blank=False, null=False)