# Generated by Django 3.2.8 on 2021-11-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20211121_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkincheckout',
            name='checked_in',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='checkincheckout',
            name='checked_out',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
