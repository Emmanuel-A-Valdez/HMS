from rest_framework import serializers
from .models import Item, ItemType


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = [
            "id",
            "item_type",
        ]


class ItemSerializer(serializers.ModelSerializer):
    item_type = serializers.SlugRelatedField(
        queryset=ItemType.objects.all(), slug_field="item_type"
    )
    image = serializers.ImageField(required=False)

    class Meta:
        model = Item
        fields = [
            "id",
            "item_type",
            "item",
            "image",
            "description",
            "price",
            "status",
        ]
