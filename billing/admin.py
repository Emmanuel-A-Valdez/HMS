from django.contrib import admin

from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    fields = [
        "booking",
        "room_fees",
        "order_fees",
        "grand_total",
        "status",
    ]

    list_display = [
        "booking",
        "date",
        "pk",
        "grand_total",
        "status",
    ]
