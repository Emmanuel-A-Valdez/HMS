from django.db import models
from rooms.models import Room, RoomType
from customers.models import Customer


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}'s reservation."
