from django.contrib import admin
from applications.models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "operation_type",
        "client_name",
        "inn",
        "status",
    )

    list_filter = (
        "operation_type",
        "payment_type",
        "status",
    )

    search_fields = (
        "client_name",
        "inn",
        "kpp",
        "contact_phone",
    )