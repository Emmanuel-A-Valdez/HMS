from django.urls import path, re_path

from .views import (
    BookingListView,
    BookingView,
    CheckInView,
    CheckOutView,
    EBookingListView,
    RoomAvialabilityView,
)

urlpatterns = [
    path("", BookingListView.as_view()),
    path("online", EBookingListView.as_view()),
    path("<int:pk>/", BookingView.as_view()),
    path(
        "available-rooms/<str:room_type>/<str:arrival>/<str:departure>/",
        RoomAvialabilityView.as_view(),
    ),
    path(
        "check-in/<int:booking>/",
        CheckInView.as_view(),
    ),
    path(
        "check-out/<int:pk>/",
        CheckOutView.as_view(),
    )
    # re_path(
    #     r"^available-rooms/<slug:room_type>/(?P<check_in>\d{4}-\d{2}-\d{2})/(?P<check_out>\d{4}-\d{2}-\d{2})/$",
    #     RoomAvialabilityView.as_view(),
    # ),
]
