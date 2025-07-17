"""
Test cases for forms in the Catalog application.

This module contains unit tests for form validation and functionality.
"""

import datetime
from django.test import TestCase
from django.utils import timezone

from catalog.forms import RenewBookForm


class RenewBookFormTest(TestCase):
    """Test case for RenewBookForm."""

    def test_renew_form_date_field_label(self):
        """Test renewal_date field label."""
        form = RenewBookForm()
        self.assertTrue(
            form.fields['renewal_date'].label is None or 
            form.fields['renewal_date'].label == 'renewal date'
        )

    def test_renew_form_date_field_help_text(self):
        """Test renewal_date field help text."""
        form = RenewBookForm()
        expected_help_text = 'Enter a date between now and 4 weeks (default 3).'
        self.assertEqual(
            form.fields['renewal_date'].help_text, 
            expected_help_text
        )

    def test_renew_form_date_in_past(self):
        """Test form validation fails for past dates."""
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        """Test form validation fails for dates too far in future."""
        date = (
            datetime.date.today() + 
            datetime.timedelta(weeks=4) + 
            datetime.timedelta(days=1)
        )
        form = RenewBookForm(data={'renewal_date': date})
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        """Test form validation passes for today's date."""
        date = datetime.date.today()
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        """Test form validation passes for maximum allowed date."""
        date = datetime.date.today() + datetime.timedelta(weeks=4)
        form = RenewBookForm(data={'renewal_date': date})
        self.assertTrue(form.is_valid())

