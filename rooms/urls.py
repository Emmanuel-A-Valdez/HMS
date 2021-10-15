from django.urls import path
from .views import RoomTypeView, RoomView

urlpatterns = [
    path("room-types", RoomTypeView.as_view()),
    path("", RoomView.as_view()),
]
