from django.contrib import admin

from .models import TurnDown


@admin.register(TurnDown)
class RoomAdmin(admin.ModelAdmin):
    fields = [
        "room_number",
        "status",
    ]

    list_display = [
        "room_number",
        "pk",
        "status",
    ]
