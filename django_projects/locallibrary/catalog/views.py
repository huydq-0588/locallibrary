from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from catalog.constants import BookInstanceStatus, PaginationSettings, ViewSettings
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
    
    # Available books (using constant from constants.py)
    num_instances_available = BookInstance.objects.filter(
        status__exact=BookInstanceStatus.AVAILABLE
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
    context_object_name = ViewSettings.BOOK_LIST_CONTEXT_NAME
    paginate_by = PaginationSettings.BOOKS_PER_PAGE

class BookDetailView(generic.DetailView):
    model = Book
    
    def get_context_data(self, **kwargs):
        """Add extra context data to the template."""
        context = super().get_context_data(**kwargs)
        
        # Get the book object
        book = self.get_object()
        
        # Pass genres to avoid database hit in template
        context['book_genres'] = book.genre.all()
        
        # Pass book instances with their status for better performance
        context['book_instances'] = book.bookinstance_set.select_related('borrower').all()
        
        # Pass status constants to template to avoid hardcoding
        context['status_available'] = BookInstanceStatus.AVAILABLE
        context['status_maintenance'] = BookInstanceStatus.MAINTENANCE
        context['status_on_loan'] = BookInstanceStatus.ON_LOAN
        context['status_reserved'] = BookInstanceStatus.RESERVED
        
        return context


# Example of how to use constants in other views
class AuthorListView(generic.ListView):
    """Example view using constants for configuration."""
    model = Author
    context_object_name = ViewSettings.AUTHOR_LIST_CONTEXT_NAME
    paginate_by = PaginationSettings.AUTHORS_PER_PAGE
    # template_name = ViewSettings.AUTHOR_LIST_TEMPLATE  # Uncomment if using custom template


class BookInstanceListView(generic.ListView):
    """Example view for book instances with filtering by status."""
    model = BookInstance
    context_object_name = ViewSettings.BOOK_INSTANCE_LIST_CONTEXT_NAME
    paginate_by = PaginationSettings.BOOK_INSTANCES_PER_PAGE
    
    def get_queryset(self):
        """Filter available book instances as an example."""
        return BookInstance.objects.filter(
            status=BookInstanceStatus.AVAILABLE
        ).order_by('due_back')
