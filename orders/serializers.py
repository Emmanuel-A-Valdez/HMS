from rest_framework import serializers
from .models import Order
from bookings.models import Booking
from bookings.serializers import BookingSerializer
from items.models import Item


class OrderSerializer(serializers.ModelSerializer):
    booking = serializers.SlugRelatedField(
        queryset=Booking.objects.all(),
        slug_field="booking_slug",
    )
    item = serializers.SlugRelatedField(
        queryset=Item.objects.all(),
        slug_field="item",
    )
    # total = serializers.DecimalField(required=False)

    class Meta:
        model = Order
        fields = [
            "id",
            "booking",
            "item",
            "date",
            "quantity",
            "total",
            "status",
        ]
        read_only_fields = ("id", "date")
