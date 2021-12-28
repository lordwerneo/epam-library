"""
This module contains rest operation for /api/index get method
"""
from flask_restful import Resource

resources = [
    {'main': {'get': 'http://localhost:5000/api'}},
    {'genres': {'get': 'http://localhost:5000/api/genres',
                'post': 'http://localhost:5000/api/genres'}},
    {'genre': {'get': 'http://localhost:5000/api/genre/<string:genre_'
                      'name>',
               'put': 'http://localhost:5000/api/genre/<string:genre_'
                      'name>',
               'delete': 'http://localhost:5000/api/genre/<string:gen'
                         're_name>'}},
    {'books': {'get': 'http://localhost:5000/api/books',
               'post': 'http://localhost:5000/api/books'}},
    {'books_genre': {'get': 'http://localhost:5000/api/books/<string'
                            ':genre_ name>'}},
    {'book': {'get': 'http://localhost:5000/api/book/<string:'
                     'book_isbn',
              'put': 'http://localhost:5000/api/book/<string:'
                     'book_isbn',
              'delete': 'http://localhost:5000/api/book/<string:'
                        'book_isbn'}}]


class Index(Resource):
    """
    Class for Index API Resource available at /api/index
    """
    # noinspection PyMethodMayBeStatic
    # pylint: disable=no-self-use
    def get(self):
        """
        Called when app at /api/index receive GET request
        :return: json of all available resource and methods
        """
        return {'resources': [resource for resource in resources]}
