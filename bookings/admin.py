from django.contrib import admin

from .models import Booking, CheckInCheckOut


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = [
        "guest",
        "room_type",
        "room_number",
        "arrival",
        "departure",
    ]

    list_display = [
        "guest",
        "pk",
        "room_type",
        "room_number",
        "arrival",
    ]


@admin.register(CheckInCheckOut)
class CheckInCheckOutAdmin(admin.ModelAdmin):
    fields = [
        "booking",
        "checked_in",
        "check_in",
        "checked_out",
        "check_out",
    ]

    list_display = [
        "booking",
        "pk",
        "checked_in",
        "checked_out",
    ]
