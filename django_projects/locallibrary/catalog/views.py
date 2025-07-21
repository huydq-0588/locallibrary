from django.shortcuts import get_object_or_404, render
from catalog.models import Book, Author, BookInstance, Genre
from catalog.constants import BookInstanceStatus, PaginationSettings, ViewSettings
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

from catalog.forms import RenewBookForm  # Sửa import path này
import datetime

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


class BookInstanceListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed.html'
    context_object_name = ViewSettings.BOOK_INSTANCE_CONTEXT_NAME
    paginate_by = PaginationSettings.BOOK_INSTANCES_PER_PAGE
    
    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user,
            status__exact=BookInstanceStatus.ON_LOAN
        ).order_by('due_back')


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)
    
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = RenewBookForm(request.POST)
        
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('my-borrowed'))
    
    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    
    context = {
        'form': form,
        'book_instance': book_instance,
    }
    
    return render(request, 'catalog/book_renew_librarian.html', context)

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death':'11/06/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
