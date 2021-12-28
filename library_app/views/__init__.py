"""
__init__.py file of views module with imported index, genres, and books.
"""
# pylint: disable=cyclic-import
from . import index
from . import genres
from . import books

index = index.index
genres = genres.genres
books = books.books
