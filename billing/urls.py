from django.urls import path

from .views import BillListView, BillView

urlpatterns = [
    path("", BillListView.as_view()),
    path("<int:pk>/", BillView.as_view()),
]
