from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# CLASE QUE LISTA LAS URLS
class ListUrls(APIView):
    """
    Return a list of all developer related urls.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):

        urls = {
            "Urls": "",
            "Employees": "------------------------------------------------------------",
            "Register": "account/register/",
            "Login": "account/login/",
            "Logout": "account/logout/",
            "User detail - Update": "account/user/",
            "ROOMS": "------------------------------------------------------------",
            "Room types": "rooms/room-types/",
            "Room type": "rooms/room-types/<int:pk>/",
            "Rooms": "rooms/",
            "Room": "rooms/<int:id>/",
            "GUESTS": "------------------------------------------------------------",
            "Guests": "guests/",
            "Guest": "guests/<int:pk>",
            "BOOKINGS": "------------------------------------------------------------",
            "Bookings": "bookings/",
            "Bookings Online": "bookings/online/",
            "Booking": "bookings/<int:pk>/",
            "Available Rooms": "bookings/available-rooms/<str:room_type>/<str:arrival>/<str:departure>/",
            "Check In": "bookings/check-in/<int:pk>",
            "Check Out": "bookings/check-out/<int:pk>",
            "HOUSEKEEPING": "------------------------------------------------------------",
            "Turndowns": "housekeeping/",
            "Turndown": "housekeeping/<int:pk>/",
            "PRODUCTS": "------------------------------------------------------------",
            "Item Types": "items/item-types/",
            "Item Type": "items/item-types/<int:pk>/",
            "Items": "items/",
            "Item": "items/<int:pk>/",
            "ORDERS": "------------------------------------------------------------",
            "Orders": "orders/",
            "Orders by Guest": "orders/guest/<int:booking>/",
            "Order": "orders/<int:pk>/",
            "BILLING": "------------------------------------------------------------",
            "Billing": "billing/",
            "Bill": "billing/<int:pk>/",
        }
        return Response(urls, status=status.HTTP_200_OK)
