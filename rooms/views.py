from re import A
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer


class RoomTypeView(APIView):
    def get(self, request):
        room_types = RoomType.objects.all()
        serializer = RoomTypeSerializer(room_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoomView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
