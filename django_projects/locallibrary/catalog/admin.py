from django.contrib import admin

from .models import Author, Book, BookInstance, Genre
from .constants import BookInstanceStatus
# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin configuration for Genre model."""
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin configuration for Author model."""
    list_display = (
        'last_name',
        'first_name', 
        'date_of_birth',
        'date_of_death'
    )
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]


class BooksInstanceInline(admin.TabularInline):
    """Inline admin configuration for BookInstance."""
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin configuration for Book model."""
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

    def display_genre(self, obj):
        """Create a string for the Genre.
        
        This is required to display genre in Admin.
        """
        return ', '.join(genre.name for genre in obj.genre.all()[:3])

    display_genre.short_description = 'Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Admin configuration for BookInstance model."""
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

