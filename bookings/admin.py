from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = [
        "guest",
        "room_type",
        "room_number",
        "arrival",
        "departure",
        "checked_in",
        "check_in",
        "checked_out",
        "check_out",
    ]

    list_display = [
        "guest",
        "pk",
        "room_type",
        "room_number",
        "arrival",
    ]
