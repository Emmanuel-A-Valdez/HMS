from django.db import models
from items.models import Item
from bookings.models import Booking


class Order(models.Model):
    ORDER_STATUS = [
        ("OUTSTANDING", "Outstanding"),
        ("PAID", "Paid"),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=50, choices=ORDER_STATUS, default="OUTSTANDING"
    )

    def __str__(self):
        return f"{self.id} - {self.booking} - {self.item}"
