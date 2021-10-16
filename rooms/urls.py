from django.urls import path

from .views import RoomListView, RoomTypeListView, RoomTypeView, RoomView

urlpatterns = [
    path("room-types/", RoomTypeListView.as_view()),
    path("room-types/<int:pk>/", RoomTypeView.as_view()),
    path("", RoomListView.as_view(), name="rooms"),
    path("<int:pk>/", RoomView.as_view()),
]
