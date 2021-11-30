from core.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer


class RoomTypeListView(APIView):
    def get(self, request):
        room_types = RoomType.objects.all()
        print(type(room_types))
        serializer = RoomTypeSerializer(room_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomTypeView(APIView):
    def get(self, request, pk):
        room = get_object_or_404(RoomType, pk=pk)
        serializer = RoomTypeSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        room = get_object_or_404(RoomType, pk=pk)
        serializer = RoomTypeSerializer(room, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        room_type = get_object_or_404(Room, pk=pk)
        room_type.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )


class RoomListView(APIView):
    def get(self, request):
        rooms = Room.objects.select_related("room_type")
        paginator = CustomPagination()
        room_list = paginator.paginate_queryset(rooms, request)
        serializer = RoomSerializer(room_list, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RoomView(APIView):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        serializer = RoomSerializer(room, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        room.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
