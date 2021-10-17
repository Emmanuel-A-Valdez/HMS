from django.urls import path

from .views import BookingListView, BookingView

urlpatterns = [
    path("", BookingListView.as_view()),
    path("<int:pk>/", BookingView.as_view()),
]
