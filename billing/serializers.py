from bookings.models import Booking
from rest_framework import serializers

from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    booking = serializers.SlugRelatedField(
        queryset=Booking.objects.all(),
        slug_field="booking_slug",
    )
    room_fees = serializers.DecimalField(max_digits=9, decimal_places=2, required=False)
    order_fees = serializers.DecimalField(
        max_digits=8, decimal_places=2, required=False
    )
    grand_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False
    )
    status = serializers.CharField(required=False)

    class Meta:
        model = Bill
        fields = [
            "id",
            "booking",
            "date",
            "room_fees",
            "order_fees",
            "grand_total",
            "status",
        ]
        read_only_fields = (
            "id",
            "date",
        )
