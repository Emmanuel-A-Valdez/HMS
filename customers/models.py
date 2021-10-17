from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    country_code = models.CharField(max_length=6, default="+1")
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"
