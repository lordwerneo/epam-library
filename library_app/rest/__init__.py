"""
__init__.py file of rest module with imported index_api, genre_api and
book_api submodules.
"""
# pylint: disable=cyclic-import
from . import index_api
from . import genre_api
from . import book_api

Index = index_api.Index
GenresList = genre_api.GenresList
GenresSolo = genre_api.GenresSolo
BooksList = book_api.BooksList
BooksGenreList = book_api.BooksGenreList
BooksSolo = book_api.BooksSolo
