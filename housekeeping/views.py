from datetime import time
from core.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rooms.models import Room

from .models import TurnDown
from .serializers import TurnDownSerializer


class TurnDownListView(APIView):
    def get(self, request):
        turndown = TurnDown.objects.select_related("room_number")
        paginator = CustomPagination()
        turndown_list = paginator.paginate_queryset(turndown, request)
        serializer = TurnDownSerializer(turndown_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        room = Room.objects.filter(room_number=request.data["room_number"]).first()
        if TurnDown.objects.filter(room_number=room).first().status == "CLEANING":
            context = {"detail": "Room is already undergoing turndown service."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        serializer = TurnDownSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TurnDownView(APIView):
    def get(self, request, pk):
        turndown = get_object_or_404(TurnDown, pk=pk)
        serializer = TurnDownSerializer(turndown)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        turndown = get_object_or_404(TurnDown, pk=pk)
        room = Room.objects.get(room_number=request.data["room_number"])

        if turndown.status == "COMPLETE":
            context = {"detail": "Turndown serivce is already complete."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        if request.data["status"] == "COMPLETE":
            turndown.finish = timezone.now()
            room.status = "Vacant"
            room.save()

        serializer = TurnDownSerializer(turndown, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, request, pk):
    #     turndown = get_object_or_404(TurnDown, pk=pk)
    #     turndown.delete()
    #     return Response(
    #         {"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
    #     )
