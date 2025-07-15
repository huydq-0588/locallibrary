from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # Index view for the catalog
    path('books/', views.BookListView.as_view(), name='books'),  # List of books
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Detail view for a book

    
]