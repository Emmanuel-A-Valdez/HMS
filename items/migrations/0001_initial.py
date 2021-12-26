# Generated by Django 3.2.8 on 2021-12-26 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('IN STOCK', 'In Stock'), ('SOLD OUT', 'Sold Out')], default=None, max_length=50)),
                ('item_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.itemtype')),
            ],
        ),
    ]
