# Generated by Django 3.2.8 on 2021-12-26 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='total',
        ),
    ]
