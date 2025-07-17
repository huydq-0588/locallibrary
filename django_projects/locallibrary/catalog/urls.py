from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index view for the catalog
    path('books/', views.BookListView.as_view(), name='books'),  # List of books
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Detail view for a book
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('mybooks/', views.BookInstanceListView.as_view(), name='my-borrowed'),  # List of borrowed books
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
