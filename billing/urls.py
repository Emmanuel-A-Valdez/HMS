from django.urls import path

from .views import AutoBillView, BillListView, BillView

urlpatterns = [
    path("", BillListView.as_view()),
    path("automatic/<int:booking>/", AutoBillView.as_view()),
    path("<int:pk>/", BillView.as_view()),
]
