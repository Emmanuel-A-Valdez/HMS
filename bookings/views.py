from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
import datetime
from .models import Booking
from .serializers import BookingSerializer
from .utils import get_available_room


class BookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.select_related("guest", "room_type", "room")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data["check_in"] < str(datetime.datetime.now()).split()[0]:
            context = {
                "error": "Check in date must be greater or equal to today's date."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["check_out"] <= request.data["check_in"]:
            context = {"error": "Check out date must be greater than check in."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        request.data["room"] = get_available_room(
            request.data["room_type"],
            request.data["check_in"],
            request.data["check_out"],
        )

        serializer = BookingSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingView(APIView):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
