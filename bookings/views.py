from datetime import datetime

from core.pagination import CustomPagination
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.models import Room, RoomType
from rooms.serializers import RoomSerializer

from .models import Booking
from .serializers import BookingSerializer, CheckInSerializer, CheckOutSerializer
from housekeeping.models import TurnDown

now = str(timezone.now()).split()[0]


class RoomAvialabilityView(APIView):
    def get(self, request, room_type, arrival, departure):
        try:
            rm_type = RoomType.objects.filter(
                room_type=room_type.replace("-", " ").title()
            )[0]
        except:
            context = {"detail": "Room type does not exist."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            datetime.strptime(arrival, "%Y-%m-%d")
        except ValueError:
            context = {"detail": "Incorrect data format, should be YYYY-MM-DD"}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            datetime.strptime(departure, "%Y-%m-%d")
        except ValueError:
            context = {"detail": "Incorrect data format, should be YYYY-MM-DD"}
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
        paginator = CustomPagination()
        booking_list = paginator.paginate_queryset(bookings, request)
        serializer = BookingSerializer(booking_list, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if request.data["arrival"] < now:
            context = {
                "detail": "Check in date must be greater or equal to today's date."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["departure"] <= request.data["arrival"]:
            context = {"detail": "Check out date must be greater than check in."}
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
                "detail": "This room is unavailable during these dates. Please choose another."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EBookingListView(APIView):
    def get(self, request):
        bookings = Booking.objects.select_related("guest", "room_type", "room_number")
        paginator = CustomPagination()
        booking_list = paginator.paginate_queryset(bookings, request)
        serializer = BookingSerializer(booking_list, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if request.data["arrival"] < now:
            context = {
                "detail": "Check in date must be greater or equal to today's date."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["departure"] <= request.data["arrival"]:
            context = {"detail": "Check out date must be greater than check in."}
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
            {"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )


class CheckInView(APIView):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = CheckInSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        room = Room.objects.get(room_number=request.data["room_number"])

        if request.data["checked_in"] and room.status == "Turndown":
            context = {
                "detail": "Turndown service is not complete yet. Please see housekeeping."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["checked_in"] and room.status == "Occupied":
            context = {"detail": "Room is unavailable. Please consult reservations."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["checked_in"] and booking.checked_in:
            context = {"detail": "Guest has already checked in."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        if request.data["checked_in"]:
            request.data["check_in"] = timezone.now()
        else:
            request.data["check_in"] = None
            booking.checked_out = False
            booking.check_out = None
            turndown = TurnDown.objects.filter(room_number=booking.room_number)[0]
            turndown.delete()

        room.status = "Occupied"
        room.save()

        if not request.data["checked_in"] and room.status == "Occupied":
            room.status = "Vacant"
            room.save()

        serializer = CheckInSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CheckOutView(APIView):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        serializer = CheckOutSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        room = Room.objects.get(room_number=booking.room_number)

        if request.data["checked_out"] and not booking.checked_in:
            context = {"detail": "Guest has not checked in yet."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["checked_out"] and booking.checked_out:
            context = {"detail": "Guest has already checked out."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        if request.data["checked_out"]:
            request.data["check_out"] = timezone.now()
        else:
            request.data["check_out"] = None

        if request.data["checked_out"]:
            room.status = "Turndown"
            room.save()
            TurnDown.objects.create(
                room_number=booking.room_number,
            )

        if not request.data["checked_out"] and room.status == "Turndown":
            room.status = "Occupied"
            room.save()
            turndown = TurnDown.objects.filter(room_number=booking.room_number)[0]
            turndown.delete()

        serializer = CheckOutSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
