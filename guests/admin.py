from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    fields = [
        "first_name",
        "last_name",
        "email",
        "country_code",
        "phone_num",
        "address",
        "city",
        "state",
        "country",
        "zip_code",
    ]

    list_display = [
        "name_slug",
        "pk",
        "email",
    ]
