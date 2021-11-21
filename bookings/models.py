from django.db import models
from rooms.models import Room, RoomType
from guests.models import Guest


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="booking", null=True, blank=True
    )
    booking_date = models.DateField(auto_now_add=True)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest.first_name} {self.guest.last_name}'s reservation."
