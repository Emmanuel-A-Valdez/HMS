from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("employees.urls")),
    path("rooms/", include("rooms.urls")),
    path("guests/", include("guests.urls")),
    path("bookings/", include("bookings.urls")),
    path("housekeeping/", include("housekeeping.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
