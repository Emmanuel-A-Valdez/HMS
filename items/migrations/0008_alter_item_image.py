# Generated by Django 3.2.8 on 2021-12-26 20:36

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to=items.models.upload_to),
        ),
    ]
