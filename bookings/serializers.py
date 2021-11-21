from rest_framework import serializers
from rooms.models import Room, RoomType
from guests.models import Guest
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.SlugRelatedField(
        queryset=Guest.objects.all(), slug_field="name_slug"
    )
    room_type = serializers.SlugRelatedField(
        queryset=RoomType.objects.all(), slug_field="room_type"
    )
    room_number = serializers.SlugRelatedField(
        queryset=Room.objects.all(), slug_field="room_number", required=False
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "guest",
            "room_type",
            "room_number",
            "booking_date",
            "check_in",
            "check_out",
        ]
