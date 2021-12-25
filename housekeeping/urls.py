from django.urls import path

from .views import TurnDownListView, TurnDownView

urlpatterns = [
    path("", TurnDownListView.as_view()),
    path("<int:pk>/", TurnDownView.as_view()),
]
