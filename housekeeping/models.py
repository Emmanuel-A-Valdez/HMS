from django.db import models
from rooms.models import Room


class TurnDown(models.Model):
    TURNDOWN_STATUS = [
        ("CLEANING", "Cleaning"),
        ("COMPLETE", "Complete"),
    ]
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, choices=TURNDOWN_STATUS, default="CLEANING"
    )
    begin = models.DateTimeField(auto_now_add=True)
    finish = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.room_number}"
