from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from catalog.constants import BookInstanceStatus
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    
    # Available books (using constants from constants module)
    num_instances_available = BookInstance.objects.filter(
        status__exact=BookInstanceStatus.AVAILABLE
    ).count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # Optional: name for template context
    paginate_by = 10  # Number of books to display per page

class BookDetailView(generic.DetailView):
    model = Book
