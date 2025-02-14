#*****************************************************************************************
#  Project name : GUTENDEX
#  Filename : views.php
#  Developed by : VIJAY
#*****************************************************************************************
from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.db.models import Q

class BookListTemplateView(TemplateView):
    """
    View to render the DataTable UI in an HTML template.
    This view does NOT handle API responses, only HTML rendering.
    """
    template_name = "books/books_list.html"


class BookFilter(filters.FilterSet):
    """
    FilterSet class for filtering books based on various fields such as:
    - Gutenberg ID
    - Language
    - Media Type
    - Topic (Subjects or Bookshelves)
    - Author
    - Title
    """
    gutenberg_id = filters.NumberFilter(field_name="gutenberg_id", lookup_expr="exact")
    language = filters.CharFilter(field_name="languages__code", lookup_expr="icontains")
    media_type = filters.CharFilter(field_name="bookformat__mime_type", lookup_expr="icontains")
    topic = filters.CharFilter(method="filter_by_topic")  # Custom filter for topics
    author = filters.CharFilter(field_name="authors__name", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["gutenberg_id", "language", "media_type", "author", "title"]

    def filter_by_topic(self, queryset, name, value):
        """
        Custom filter method that filters books based on topics.
        Searches in both `subjects` and `bookshelves` fields.

        :param queryset: The queryset of books
        :param name: The filter field name
        :param value: The search value
        :return: Filtered queryset
        """
        return queryset.filter(
            Q(subjects__name__icontains=value) | 
            Q(bookshelves__name__icontains=value)
        ).distinct()


class BookListView(APIView):
    """
    API View for retrieving books with pagination, sorting, and filtering.
    This API is used by the DataTable frontend.

    Supports the following filters:
    - Gutenberg ID
    - Language
    - Media Type
    - Topic (Subjects or Bookshelves)
    - Author
    - Title

    Supports sorting and pagination.
    """
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ["title", "authors__name", "subjects__name", "bookshelves__name"]
    ordering_fields = ["download_count"]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests for the book list API.
        Extracts filters, pagination, and sorting parameters from the request.

        :param request: The HTTP request object
        :return: JSON response with book data formatted for DataTables
        """
        queryset = Book.objects.all().order_by("-download_count")  # Default: sort by downloads

        # Extract DataTable parameters
        draw = int(request.GET.get("draw", 1))  # Unique request ID for DataTables
        start = int(request.GET.get("start", 0))  # Pagination start index
        length = int(request.GET.get("length", 25))  # Number of records per page

        # Extract sorting parameters
        order_column_index = request.GET.get("order[0][column]", "0")
        order_direction = request.GET.get("order[0][dir]", "asc")

        column_map = {
            "0": "title",
            "1": "authors__name",
            "2": "languages__code",
            "3": "subjects__name",
            "4": "bookshelves__name",
            "5": "media_type",
            "6": "download_count"
        }

        # Apply sorting if a valid column index is provided
        if order_column_index in column_map:
            order_column = column_map[order_column_index]
            if order_direction == "desc":
                order_column = f"-{order_column}"
            queryset = queryset.order_by(order_column)

        # Apply search filter
        search_value = request.GET.get("search[value]", "").strip()
        if search_value:
            queryset = queryset.filter(
                Q(title__icontains=search_value) |
                Q(authors__name__icontains=search_value) |
                Q(subjects__name__icontains=search_value) |
                Q(bookshelves__name__icontains=search_value)
            ).distinct()

        # Apply pagination
        total_records = queryset.count()
        queryset = queryset[start: start + length]

        # Serialize book data
        serializer = BookSerializer(queryset, many=True)

        # Return JSON response formatted for DataTables
        return Response({
            "draw": draw,
            "recordsTotal": total_records,
            "recordsFiltered": total_records,
            "data": serializer.data,
        })
