# Generated by Django 3.2.8 on 2021-12-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='placeholder.png', null=True, upload_to='media/items/'),
        ),
    ]