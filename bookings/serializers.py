from rest_framework import serializers
from rooms.models import Room, RoomType
from customers.models import Customer
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        queryset=Customer.objects.all(), slug_field="email"
    )
    room_type = serializers.SlugRelatedField(
        queryset=RoomType.objects.all(), slug_field="room_type"
    )
    room = serializers.SlugRelatedField(
        queryset=Room.objects.all(), slug_field="room_number"
    )

    class Meta:
        model = Booking
        fields = [
            "id",
            "customer",
            "room_type",
            "room",
            "booking_date",
            "check_in",
            "check_out",
        ]
