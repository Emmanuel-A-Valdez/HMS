from django.urls import path

from .views import CustomerListView, CustomerView

urlpatterns = [
    path("", CustomerListView.as_view()),
    path("<int:pk>/", CustomerView.as_view()),
]
