from rest_framework import serializers

from .models import Room, RoomType


class RoomTypeSerializer(serializers.HyperlinkedModelSerializer):
    room_img = serializers.ImageField(required=False)

    class Meta:
        model = RoomType
        fields = [
            "id",
            "room_type",
            "room_img",
            "description",
            "price",
        ]


class RoomSerializer(serializers.ModelSerializer):
    room_type = serializers.SlugRelatedField(
        queryset=RoomType.objects.all(), slug_field="room_type"
    )

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
