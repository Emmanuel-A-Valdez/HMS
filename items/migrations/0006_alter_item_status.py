# Generated by Django 3.2.8 on 2021-12-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_alter_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('IN STOCK', 'In Stock'), ('SOLD OUT', 'Sold Out')], default='', max_length=50),
        ),
    ]
