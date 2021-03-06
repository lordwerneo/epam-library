"""
This module contains REST operations to work with books.
"""
# pylint: disable=cyclic-import
from flask_restful import Resource, reqparse
from library_app.service import book_service

book_args = reqparse.RequestParser()
book_args.add_argument('isbn', type=str, help='ISBN required', required=True)
book_args.add_argument('title', type=str, help='Title required',
                       required=True)
book_args.add_argument('author', type=str, help='Author required',
                       required=True)
book_args.add_argument('year', type=int, help='Year required', required=True)
book_args.add_argument('publisher', type=str, help='Publisher required',
                       required=True)
book_args.add_argument('copies', type=int, help='Copies required',
                       required=True)
book_args.add_argument('genre', type=str, help='Genre required', required=True)


# pylint: disable=too-many-boolean-expressions
def input_validator(args):
    """
    Method to check input arguments to suit data in books table.
    :param args: arguments to check
    :return: False if checked successfully, else True
    """
    if args['isbn'] == '' or args['title'] == '' or args['author'] == '' \
            or args['year'] < 1900 or args['year'] > 2022 or \
            args['publisher'] == '' or args['copies'] < 1 or \
            args['copies'] > 999 or args['genre'] == '' or \
            book_service.isbn_checker(args['isbn']) or \
            len(args['isbn']) < 10 or len(args['isbn']) > 20 or \
            len(args['title']) < 1 or len(args['title']) > 64 or \
            len(args['author']) < 1 or len(args['author']) > 64 or \
            len(args['publisher']) < 1 or len(args['publisher']) > 64 or \
            len(args['genre']) < 1 or len(args['genre']) > 20:
        return True
    return False


class BooksList(Resource):
    """
    Class for BookList API Resource available at /api/books
    """
    @staticmethod
    def get():
        """
        Called when GET request is received
        :return: json of all books if success or error message if no books in
        books table
        """
        books = book_service.get_all_books()
        if books == 'Error':
            return {'Message': 'No books in DB'}, 200
        return {'books': books}

    @staticmethod
    def post():
        """
        Called when POST request is received
        :return: json with information and link of created book if success or
        error
        """
        args = book_args.parse_args()
        if input_validator(args):
            return {'Message': 'Wrong data input'}, 400
        books = book_service.post_book(isbn=args['isbn'], title=args['title'],
                                       author=args['author'],
                                       year=args['year'],
                                       publisher=args['publisher'],
                                       copies=args['copies'],
                                       genre=args['genre'])
        if books == 'ISBN exists':
            return {'Message': f'Book {args["isbn"]} already exists',
                    'link': f'/api/book/{args["isbn"]}'}, 405
        if books == 'No genre':
            return {'Message': f'Genre {args["genre"]} not found'}
        return {'book': args, 'link': f'/api/book/{args["isbn"]}'}, 201


class BooksGenreList(Resource):
    """
    Class for BooksGenreList API Resource available
    at /api/books/<string:genre>'
    """
    @staticmethod
    def get(genre):
        """
        Called when get request is received
        :param genre: genre of books to look for
        :return: json of all books in a certain genre if success or error
        message
        """
        books = book_service.get_genre_books(genre)
        if books == 'Error':
            return {'Message': f'No books in {genre}'}, 404
        if books == 'No genre':
            return {'Message': f'No {genre} genre'}, 404
        return {'books': books}, 200


class BooksSolo(Resource):
    """Class for BooksSolo API Resource available at /api/book/<string:isbn>"""
    @staticmethod
    def get(isbn):
        """
        Called when get request is received
        :param isbn: unique isbn of a book
        :return: json with information about book if success or error message
        """
        book = book_service.get_book_by_isbn(isbn)
        if book == 'Error':
            return {'Message': 'No such book'}, 404
        return {'book': book}, 200

    @staticmethod
    def put(isbn):
        """
        Called when put request is received.
        :param isbn: unique isbn of a book
        :return: json with information about created book if no such book in
        table and success, json with information about updated book if book
        in table and success, or error message
        """
        args = book_args.parse_args()
        if input_validator(args):
            return {'Message': 'Wrong data input'}, 400
        book = book_service.put_book(cur_isbn=isbn,
                                     isbn=args['isbn'], title=args['title'],
                                     author=args['author'], year=args['year'],
                                     publisher=args['publisher'],
                                     copies=args['copies'],
                                     genre=args['genre'])
        if book == 'No genre':
            return {'Message': f'Genre {args["genre"]} not found'}, 404
        if book == 'ISBN exists':
            return {'Message': f'Book {args["isbn"]} already exists',
                    'link': f'/api/book/{args["isbn"]}'}, 405
        if book == 'Updated':
            return {'Message': f'Book {args["isbn"]} updated',
                    'book': args,
                    'link': f'/api/book/{args["isbn"]}'}, 200
        return {'book': args, 'link': f'/api/book/{args["isbn"]}'}, 201

    @staticmethod
    def delete(isbn):
        """
        Called when DELETE request is received
        :param isbn: unique isbn of a book
        :return: json with success message if success, or error message if no
        book in table
        """
        book = book_service.delete_book(isbn)
        if book == 'Error':
            return {'Message': 'No such book'}, 404
        return {'Message': f'Book {isbn} deleted.'}, 200
