from django.urls import path

from .views import ItemListView, ItemTypeListView, ItemTypeView, ItemView

urlpatterns = [
    path("item-types/", ItemTypeListView.as_view()),
    path("item-types/<int:pk>/", ItemTypeView.as_view()),
    path("", ItemListView.as_view(), name="rooms"),
    path("<int:pk>/", ItemView.as_view()),
]
