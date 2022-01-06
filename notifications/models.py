from django.db import models


def upload_to(instance, filename):
    return f"rooms/{filename}"


class Notification(models.Model):
    NOTIFICATION_TYPE = [
        ("Reservation", "Reservation"),
        ("Check In", "Check In"),
        ("Check Out", "Check Out"),
        ("Housekeeping", "Housekeeping"),
    ]

    type = models.CharField(
        max_length=150, choices=NOTIFICATION_TYPE, blank=True, null=True
    )
    text = models.CharField(max_length=150, blank=True, null=True)
    link = models.CharField(max_length=150, blank=True, null=True)
    seen = models.BooleanField(verbose_name="seen", default=False)
    image = models.ImageField(upload_to=upload_to, default="placeholder.png")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f" Num: {self.id} - Type: {self.type}"
