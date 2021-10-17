from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import CustomerSerializer


class CustomerListView(APIView):
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
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerView(APIView):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(
            {"message": "Successfully deleted."}, status=status.HTTP_204_NO_CONTENT
        )
