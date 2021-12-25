from django.db import models
from bookings.models import Booking
from orders.models import Order


class Bill(models.Model):
    BILL_STATUS = [
        ("OUTSTANDING", "Outstanding"),
        ("PAID", "Paid"),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    room_fees = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    order_fees = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True
    )
    grand_total = models.DecimalField(
        max_digits=9, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(max_length=50, choices=BILL_STATUS, default="OUTSTANDING")
