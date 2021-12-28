"""
__init__.py file of forms module with imported genre and book forms
"""
# pylint: disable=cyclic-import
from . import genre_form
from . import book_form

AddGenreForm = genre_form.AddGenreForm
UpdateGenreForm = genre_form.UpdateGenreForm
AddBookForm = book_form.AddBookForm
UpdateBookForm = book_form.UpdateBookForm
FilterBookForm = book_form.FilterBookForm
