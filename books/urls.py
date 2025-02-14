from django.urls import path
from .views import BookListView, BookListTemplateView

urlpatterns = [
    path("books/", BookListTemplateView.as_view(), name="book-list"),  # Renders HTML page
    path("api/books/", BookListView.as_view(), name="book-api"),  # API for DataTable AJAX
]
