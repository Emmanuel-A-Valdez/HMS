from bookings.models import Booking
from core.pagination import CustomPagination
from django.shortcuts import get_object_or_404
from orders.models import Order
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bill
from .serializers import BillSerializer


class BillListView(APIView):
    def get(self, request):
        bills = Bill.objects.select_related("booking")
        paginator = CustomPagination()
        bill_list = paginator.paginate_queryset(bills, request)
        serializer = BillSerializer(bill_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BillView(APIView):
    def get(self, request, pk):
        room_type = get_object_or_404(Bill, pk=pk)
        serializer = BillSerializer(room_type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        room_type = get_object_or_404(Bill, pk=pk)
        serializer = BillSerializer(room_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        room_type = get_object_or_404(Bill, pk=pk)
        room_type.delete()
        return Response(
            {"detail": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
