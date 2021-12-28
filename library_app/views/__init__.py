"""
__init__.py file of views module with imported index, genres, and books.
"""
from . import index
from . import genres
from . import books

index = index.index
genres = genres.genres
books = books.books
