from django.urls import path

from .views import GuestListView, GuestView

urlpatterns = [
    path("", GuestListView.as_view()),
    path("<int:pk>/", GuestView.as_view()),
]
