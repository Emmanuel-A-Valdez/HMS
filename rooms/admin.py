from django.contrib import admin
from .models import Room, RoomType


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    fields = [
        "room_type",
        "room_img",
        "description",
        "price",
    ]

    list_display = [
        "room_type",
        "pk",
    ]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = [
        "room_type",
        "room_number",
        "room_floor",
        "description",
        "status",
    ]

    list_display = [
        "room_number",
        "pk",
        "room_type",
        "room_floor",
    ]
