"""
__init__.py file of service module with imported genre_service and
book_service submodules.
"""
# pylint: disable=cyclic-import
from . import genre_service
from . import book_service
