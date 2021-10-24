from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("employees.urls")),
    path("rooms/", include("rooms.urls")),
    path("guests/", include("guests.urls")),
    path("bookings/", include("bookings.urls")),
]
