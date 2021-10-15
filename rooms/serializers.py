from .models import Room, RoomType
from rest_framework import serializers


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = [
            "id",
            "room_type",
            "room_img",
            "description",
            "cost",
        ]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "room_type",
            "room_number",
            "room_floor",
            "description",
            "status",
        ]
