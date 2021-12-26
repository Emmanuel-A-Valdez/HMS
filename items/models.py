from django.db import models


def upload_to(instance, filename):
    return f"items/{filename}"


class ItemType(models.Model):
    item_type = models.CharField(max_length=150)

    def __str__(self):
        return self.item_type


class Item(models.Model):
    ITEM_STATUS = [
        ("IN STOCK", "In Stock"),
        ("SOLD OUT", "Sold Out"),
    ]
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True)
    item = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to, default="placeholder.png")
    status = models.CharField(max_length=50, choices=ITEM_STATUS, default="")

    def __str__(self):
        return self.item
