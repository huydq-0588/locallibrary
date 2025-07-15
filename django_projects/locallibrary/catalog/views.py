from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    # Available books (using model constant instead of hardcoding)
    num_instances_available = BookInstance.objects.filter(
        status__exact=BookInstance.AVAILABLE
    ).count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # Optional: name for template context
    paginate_by = 10  # Number of books to display per page

class BookDetailView(generic.DetailView):
    model = Book
