from django.db import models


class ItemType(models.Model):
    item_type = models.CharField(max_length=150)


class Item(models.Model):
    ITEM_STATUS = [
        ("IN STOCK", "In Stock"),
        ("SOLD OUT", "Sold Out"),
    ]
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=ITEM_STATUS, default=None)
