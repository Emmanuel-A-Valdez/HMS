from django.contrib import admin
from .models import Item, ItemType


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    fields = [
        "item_type",
    ]

    list_display = [
        "item_type",
        "pk",
    ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = [
        "item_type",
        "item",
        "price",
        "image",
        "description",
        "status",
    ]

    list_display = [
        "item",
        "pk",
        "item_type",
    ]
