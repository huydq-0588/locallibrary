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
