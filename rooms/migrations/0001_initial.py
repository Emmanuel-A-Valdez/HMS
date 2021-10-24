# Generated by Django 3.2.8 on 2021-10-24 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=100, unique=True)),
                ('room_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=6)),
                ('room_floor', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('VACANT', 'Vacant'), ('OCCUPIED', 'Ocupied'), ('TURNDOWN', 'Turndown'), ('REMODELING', 'Remodeling')], default='Vacant', max_length=50)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtype')),
            ],
            options={
                'ordering': ['room_number'],
            },
        ),
    ]
