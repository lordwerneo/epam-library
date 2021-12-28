"""
__init__.py file of models module with imported genre and book submodules
"""
# pylint: disable=cyclic-import
from . import genre
from . import book

Genre = genre.Genre
Book = book.Book
