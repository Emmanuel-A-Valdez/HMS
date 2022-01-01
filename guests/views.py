from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.pagination import CustomPagination

from .models import Guest
from .serializers import GuestSerializer


class GuestListView(APIView):
    """
    {
        "first_name": "Joe",
        "last_name": "Smith",
        "email": "joesmith@test.com",
        "country_code": "+1",
        "phone_num": "6193319876",
        "address": "1345 N. Laurel St.",
        "city": "San Diego",
        "country": "United States",
        "zip_code": "92029"
    }
    """

    def get(self, request):
        guests = Guest.objects.all()
        paginator = CustomPagination()
        guest_list = paginator.paginate_queryset(guests, request)
        serializer = GuestSerializer(guest_list, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GuestView(APIView):
    def get(self, request, pk):
        guest = get_object_or_404(Guest, pk=pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        guest = get_object_or_404(Guest, pk=pk)
        serializer = GuestSerializer(guest, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        guest = get_object_or_404(Guest, pk=pk)
        guest.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
