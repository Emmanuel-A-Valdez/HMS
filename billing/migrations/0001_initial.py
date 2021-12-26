# Generated by Django 3.2.8 on 2021-12-26 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('room_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('order_fees', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('grand_total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.CharField(choices=[('OUTSTANDING', 'Outstanding'), ('PAID', 'Paid')], default='OUTSTANDING', max_length=50)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
            ],
        ),
    ]
