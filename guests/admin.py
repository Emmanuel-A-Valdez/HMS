from django.contrib import admin
from .models import Guest


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    fields = [
        "first_name",
        "last_name",
        "guest_slug",
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
        "guest_slug",
        "pk",
        "email",
    ]
