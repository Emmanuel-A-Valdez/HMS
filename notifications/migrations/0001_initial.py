# Generated by Django 3.2.8 on 2022-01-06 12:45

from django.db import migrations, models
import notifications.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Reservation', 'Reservation'), ('Check In', 'Check In'), ('Check Out', 'Check Out'), ('Housekeeping', 'Housekeeping')], max_length=150, null=True)),
                ('text', models.CharField(blank=True, max_length=150, null=True)),
                ('link', models.CharField(blank=True, max_length=150, null=True)),
                ('seen', models.BooleanField(default=False, verbose_name='seen')),
                ('image', models.ImageField(default='placeholder.png', upload_to=notifications.models.upload_to)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
