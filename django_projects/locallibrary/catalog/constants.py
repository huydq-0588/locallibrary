"""
Constants for the Catalog application.

This module contains all the constants used across the catalog app
to ensure consistency and easy maintenance.
"""

# BookInstance loan status constants
class BookInstanceStatus:
    """Constants for BookInstance status choices."""
    MAINTENANCE = 'm'
    ON_LOAN = 'o'
    AVAILABLE = 'a'
    RESERVED = 'r'
    
    # Choices tuple for Django model field
    CHOICES = (
        (MAINTENANCE, 'Maintenance'),
        (ON_LOAN, 'On loan'),
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
    )
    
    # List of all status values for easy iteration
    ALL_STATUS = [MAINTENANCE, ON_LOAN, AVAILABLE, RESERVED]
    
    # Human-readable mapping
    STATUS_LABELS = {
        MAINTENANCE: 'Maintenance',
        ON_LOAN: 'On loan', 
        AVAILABLE: 'Available',
        RESERVED: 'Reserved',
    }


# Pagination settings
class PaginationSettings:
    """Constants for pagination settings across views."""
    DEFAULT_PAGE_SIZE = 10
    BOOKS_PER_PAGE = 10
    AUTHORS_PER_PAGE = 15
    BOOK_INSTANCES_PER_PAGE = 20
    MAX_PAGE_SIZE = 100


# View settings
class ViewSettings:
    """Constants for view configuration."""
    BOOK_LIST_CONTEXT_NAME = 'book_list'
    AUTHOR_LIST_CONTEXT_NAME = 'author_list'
    BOOK_INSTANCE_CONTEXT_NAME = 'bookinstance_list'
    
    # Template names (if needed)
    BOOK_LIST_TEMPLATE = 'catalog/book_list.html'
    AUTHOR_LIST_TEMPLATE = 'catalog/author_list.html'
    BOOK_INSTANCE_TEMPLATE = 'catalog/bookinstance_list_borrowed.html'

