from django.urls import path

from .views import GuestOrderListView, OrderListView, OrderView

urlpatterns = [
    path("", OrderListView.as_view()),
    path("guest/<int:booking>", GuestOrderListView.as_view()),
    path("<int:pk>", OrderView.as_view()),
]
