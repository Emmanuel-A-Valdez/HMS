# Generated by Django 3.2.8 on 2021-10-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_remove_customer_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country_code',
            field=models.CharField(default='+1', max_length=6),
        ),
    ]
