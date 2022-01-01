from django.db import models
from rooms.models import Room, RoomType
from guests.models import Guest


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="booking", null=True, blank=True
    )
    arrival = models.DateField()
    departure = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    checked_in = models.BooleanField(null=True, blank=True, default=False)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    checked_out = models.BooleanField(null=True, blank=True, default=False)
    booking_slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.booking_slug = (
            f"Ref: {self.id} - {self.guest.first_name} {self.guest.last_name}"
        )
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.guest.first_name} {self.guest.last_name}'s reservation."


# class CheckInCheckOut(models.Model):
#     booking = models.ForeignKey(
#         Booking, on_delete=models.CASCADE, null=True, blank=True
#     )
#     checked_in = models.BooleanField(null=True, blank=True, default=False)
#     check_in = models.DateTimeField(null=True, blank=True)
#     check_out = models.DateTimeField(null=True, blank=True)
#     checked_out = models.BooleanField(null=True, blank=True, default=False)

#     def __str__(self):
#         return f"{self.booking}"
