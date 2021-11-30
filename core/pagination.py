from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    page_size_query_param = "num"
