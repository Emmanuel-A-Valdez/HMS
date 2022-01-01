from core.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from items.models import Item
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.select_related("booking", "item")
        paginator = CustomPagination()
        order_list = paginator.paginate_queryset(orders, request)
        serializer = OrderSerializer(order_list, many=True)
        return paginator.get_paginated_response(serializer.data)


class GuestOrderListView(APIView):
    def get(self, request, booking):
        orders = Order.objects.select_related("booking", "item").filter(booking=booking)
        paginator = CustomPagination()
        order_list = paginator.paginate_queryset(orders, request)
        serializer = OrderSerializer(order_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if Item.objects.filter(item=request.data["item"]):
            item_price = Item.objects.filter(item=request.data["item"])[0].price
            request.data["total"] = item_price * request.data["quantity"]
        else:
            context = {"detail": "Item does not exist."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderView(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        if Item.objects.filter(item=request.data["item"]):
            item_price = Item.objects.filter(item=request.data["item"])[0].price
            request.data["total"] = item_price * request.data["quantity"]
        else:
            context = {"detail": "Item does not exist."}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
