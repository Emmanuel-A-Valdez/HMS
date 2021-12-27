from django.urls import path
from .views import OrderListView, OrderView

urlpatterns = [
    path("", OrderListView.as_view()),
    path("<int:pk>", OrderView.as_view()),
]
