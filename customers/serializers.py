from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "country_code",
            "phone_num",
            "address",
            "city",
            "country",
            "zip_code",
        ]
