from guests.models import Guest
from bookings.models import Booking
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Guest)
def post_savecreate_guest_slug(sender, instance, created, *args, **kwargs):
    if created:
        guest = Guest.objects.filter(id=instance.id).first()
        guest.guest_slug = (
            f"Ref: {instance.id} - {instance.first_name} {instance.last_name}"
        )
        guest.save()


@receiver(post_save, sender=Booking)
def post_save_create_booking_slug(sender, instance, created, *args, **kwargs):
    if created:
        booking = Booking.objects.filter(id=instance.id).first()
        booking.booking_slug = f"Ref: {instance.id} - {instance.guest}"
        booking.save()
