from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.models import Room, RoomType
from rooms.serializers import RoomSerializer

from .models import Booking, CheckInCheckOut
from .serializers import BookingSerializer, CheckInCheckOutSerializer

now = str(timezone.now()).split()[0]


class RoomAvialabilityView(APIView):
    def get(self, request, room_type, arrival, departure):
        try:
            rm_type = RoomType.objects.filter(
                room_type=room_type.replace("-", " ").title()
            )[0]
        except:
            context = {"error": "Room type does not exist."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            datetime.strptime(arrival, "%Y-%m-%d")
        except ValueError:
            context = {"error": "Incorrect data format, should be YYYY-MM-DD"}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            datetime.strptime(departure, "%Y-%m-%d")
        except ValueError:
            context = {"error": "Incorrect data format, should be YYYY-MM-DD"}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        rooms = (
            Room.objects.select_related("room_type")
            .filter(room_type=rm_type)
            .exclude(
                Q(
                    booking__arrival__gte=arrival,
                    booking__departure__lte=departure,
                )
                | Q(
                    booking__arrival__lte=arrival,
                    booking__departure__gte=arrival,
                )
                | Q(
                    booking__arrival__lte=departure,
                    booking__departure__gte=departure,
                )
            )
        )
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.select_related("guest", "room_type", "room_number")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data["arrival"] < now:
            context = {
                "error": "Check in date must be greater or equal to today's date."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["departure"] <= request.data["arrival"]:
            context = {"error": "Check out date must be greater than check in."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        room = Room.objects.filter(room_number=request.data["room_number"])[0]
        if Booking.objects.select_related("guest", "room_type", "room_number").filter(
            Q(room_number=room)
            & Q(
                arrival__gte=request.data["arrival"],
                departure__lte=request.data["departure"],
            )
            | Q(room_number=room)
            & Q(
                arrival__lte=request.data["arrival"],
                departure__gte=request.data["arrival"],
            )
            | Q(room_number=room)
            & Q(
                arrival__lte=request.data["departure"],
                departure__gte=request.data["departure"],
            )
        ):
            context = {
                "error": "This room is unavailable during these dates. Please choose another."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EBookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.select_related("guest", "room_type", "room_number")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data["arrival"] < now:
            context = {
                "error": "Check in date must be greater or equal to today's date."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["departure"] <= request.data["arrival"]:
            context = {"error": "Check out date must be greater than check in."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        rm_type = RoomType.objects.filter(room_type=request.data["room_type"])[0]
        qs = (
            Room.objects.select_related("room_type")
            .filter(room_type=rm_type)
            .exclude(
                Q(
                    booking__arrival__gte=request.data["arrival"],
                    booking__departure__lte=request.data["departure"],
                )
                | Q(
                    booking__arrival__lte=request.data["arrival"],
                    booking__departure__gte=request.data["arrival"],
                )
                | Q(
                    booking__arrival__lte=request.data["departure"],
                    booking__departure__gte=request.data["departure"],
                )
            )
        )

        request.data["room_number"] = qs[0].room_number

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


class CheckInView(APIView):
    def get(self, request, booking):
        check_in = CheckInCheckOut.objects.all()
        serializer = CheckInCheckOutSerializer(check_in, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, booking):
        if CheckInCheckOut.objects.filter(Q(booking=booking) & Q(checked_in=True)):
            context = {"error": "Guest has already checked in."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        request.data["booking"] = booking
        request.data["check_in"] = timezone.now()
        serializer = CheckInCheckOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckOutView(APIView):
    def get(self, request, pk):
        booking = get_object_or_404(CheckInCheckOut, pk=pk)
        serializer = CheckInCheckOutSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        booking = get_object_or_404(CheckInCheckOut, pk=pk)

        if CheckInCheckOut.objects.filter(
            Q(booking=booking.booking) & Q(checked_out=True)
        ):
            context = {"error": "Guest has already checked out."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        request.data["check_out"] = timezone.now()
        serializer = CheckInCheckOutSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
