from rest_framework import serializers
from rooms.models import Room

from .models import TurnDown


class TurnDownSerializer(serializers.ModelSerializer):
    room_number = serializers.SlugRelatedField(
        queryset=Room.objects.all(), slug_field="room_number", required=False
    )

    class Meta:
        model = TurnDown
        fields = [
            "id",
            "room_number",
            "begin",
            "finish",
            "status",
        ]
        read_only_fields = (
            "id",
            "status",
        )
