from django.db import models


def upload_to(instance, filename):
    return f"rooms/{filename}"


class RoomType(models.Model):
    room_type = models.CharField(max_length=100, unique=True)
    room_img = models.ImageField(upload_to=upload_to, default="placeholder.png")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.room_type}"


class Room(models.Model):
    ROOM_STATUS = [
        ("VACANT", "Vacant"),
        ("OCCUPIED", "Occupied"),
        ("TURNDOWN", "Turndown"),
        ("REMODELING", "Remodeling"),
    ]
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=6)
    room_floor = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=ROOM_STATUS, default="Vacant")

    class Meta:
        ordering = ["room_number"]

    def __str__(self):
        return f"{self.room_number}"
