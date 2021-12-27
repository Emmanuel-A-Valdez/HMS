from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = [
        "booking",
        "item",
        "quantity",
        "total",
        "status",
    ]

    list_display = [
        "item",
        "pk",
        "booking",
        "date",
    ]
