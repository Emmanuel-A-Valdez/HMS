from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = [
        "booking_slug",
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
        "booking_slug",
        "pk",
        "room_type",
        "room_number",
        "arrival",
    ]
