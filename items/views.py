from core.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item, ItemType
from .serializers import ItemSerializer, ItemTypeSerializer


class ItemTypeListView(APIView):
    def get(self, request):
        item_types = ItemType.objects.all()
        paginator = CustomPagination()
        item_type_list = paginator.paginate_queryset(item_types, request)
        serializer = ItemTypeSerializer(item_type_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ItemTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemTypeView(APIView):
    def get(self, request, pk):
        item_type = get_object_or_404(ItemType, pk=pk)
        serializer = ItemTypeSerializer(item_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        item_type = get_object_or_404(ItemType, pk=pk)
        serializer = ItemTypeSerializer(item_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        item_type = get_object_or_404(ItemType, pk=pk)
        item_type.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )


class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.select_related("item_type")
        paginator = CustomPagination()
        item_list = paginator.paginate_queryset(items, request)
        serializer = ItemSerializer(item_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
