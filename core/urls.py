from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("employees.urls")),
    path("rooms/", include("rooms.urls")),
    path("guests/", include("guests.urls")),
    path("bookings/", include("bookings.urls")),
    path("housekeeping/", include("housekeeping.urls")),
    path("products/", include("items.urls")),
    path("orders/", include("orders.urls")),
    path("billing/", include("billing.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
