# Generated by Django 3.2.8 on 2021-11-20 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_alter_booking_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='room',
            new_name='room_number',
        ),
    ]