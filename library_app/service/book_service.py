"""
This module contains CRUD operations to work with 'books' table.
"""
# pylint: disable=cyclic-import
import re
from library_app import db
from ..models import Genre, Book


# pylint: disable=too-many-return-statements
# pylint: disable=too-many-branches
def isbn_checker(isbn):
    """
    Check ISBN for invalid characters, length, format and checksum.
    """
    # Check for invalid characters
    if re.search(r'[\d-]+[0-9X]$', isbn).group() != isbn:
        return 'Invalid characters'
    # Strip of redundant characters
    isbn_filtered = ''.join(re.findall(r'[\dX]+', isbn)) \
        if isbn[-1] == 'X' and len(isbn) == 13 \
        else ''.join(re.findall(r'[\d]+', isbn))
    if len(isbn_filtered) == 10:
        # Check for invalid format
        if isbn.count('-') == 3:
            checksum = 0
            for index, value in enumerate(isbn_filtered[:-1]):
                checksum += int(value) * (10-index)
            checksum = 11 - (checksum % 11)
            if checksum == 11:
                checksum = 0
            elif checksum == 10:
                checksum = 'X'
            # Check for invalid checksum
            if str(checksum) != isbn[-1]:
                return 'Invalid checksum'
        else:
            return 'Invalid format'
    elif len(isbn_filtered) == 13:
        # Check for invalid format
        if isbn.count('-') == 4:
            checksum = 0
            for index, value in enumerate(isbn_filtered[:-1]):
                if index % 2 == 0:
                    checksum += int(value)
                else:
                    checksum += 3 * int(value)
            checksum = 10 - checksum % 10
            if str(checksum) != isbn[-1]:
                return 'Invalid checksum'
        else:
            return 'Invalid format'
    else:
        return 'Invalid length'
    return None


# pylint: disable=no-member
def get_all_books():
    """
    Select all records from books table.
    :return: List of dicts of books
    """
    books = Book.query.all()
    if books:
        return [book.to_dict() for book in books]
    return 'Error'


# pylint: disable=no-member
def get_genre_books(genre):
    """
    Select all books of genre from books table.
    :param genre: genre of the books to return
    :return: List of dicts of books of genre
    """
    genre = Genre.query.filter_by(name=genre).first()
    if not genre:
        return 'No genre'
    books = Book.query.filter_by(genre_id=genre.id).all()
    if books:
        return [book.to_dict() for book in books]
    return 'Error'


# pylint: disable=no-member
def get_filtered_books(year_start, year_end, genre):
    """
    Select all books from books table filtered by year from, year to, and
    genre.
    :param year_start: year to filter from
    :param year_end: year to filter to
    :param genre: genre to filter by
    :return: list of dicts of books with applied filter
    """
    books = Book.query
    if year_start:
        books = books.filter(Book.year >= int(year_start))
    if year_end:
        books = books.filter(Book.year <= int(year_end))
    if int(genre) > 0:
        books = books.filter(Book.genre_id == int(genre))
    books = [book.to_dict() for book in books]
    return books


# pylint: disable=no-member
# pylint: disable=inconsistent-return-statements
# pylint: disable=too-many-arguments
def post_book(isbn, title, author, year, publisher, copies, genre):
    """
    Add new book to table
    :param isbn: unique isbn of the book
    :param title: title of the book
    :param author: author of the book
    :param year: year published
    :param publisher: publisher of the book
    :param copies: copies of the book available
    :param genre: genre of the book
    :return: None if success, else error message
    """
    genre_id = Genre.query.filter_by(name=genre).first()
    book = Book.query.filter_by(isbn=isbn).first()
    if genre_id:
        if not book:
            book = Book(isbn=isbn, title=title, author=author, year=year,
                        publisher=publisher, copies=copies,
                        genre_id=genre_id.id)
            db.session.add(book)
            db.session.commit()
            return
        return 'ISBN exists'
    return 'No genre'


# pylint: disable=no-member
# pylint: disable=inconsistent-return-statements
# pylint: disable=too-many-arguments
def put_book(cur_isbn, isbn, title, author, year, publisher, copies, genre):
    """
    Update an existing book or create a new one.
    :param cur_isbn: unique isbn of the book to update
    :param isbn: unique isbn of the book
    :param title: title of the book
    :param author: author of the book
    :param year: year published
    :param publisher: publisher of the book
    :param copies: copies of the book available
    :param genre: genre of the book
    :return: None if success, else error message
    """
    genre_id = Genre.query.filter_by(name=genre).first()
    if genre_id:
        book = Book.query.filter_by(isbn=cur_isbn).first()
        if not book:
            new_book = Book.query.filter_by(isbn=isbn).first()
            if not new_book:
                new_book = Book(isbn=isbn, title=title, author=author,
                                year=year, publisher=publisher, copies=copies,
                                genre_id=genre_id.id)
                db.session.add(new_book)
                db.session.commit()
                return
            return 'ISBN exists'
        book.title = title
        book.author = author
        book.year = year
        book.publisher = publisher
        book.copies = copies
        book.genre_id = genre_id.id
        db.session.commit()
        return 'Updated'
    return 'No genre'


# pylint: disable=no-member
# pylint: disable=inconsistent-return-statements
def delete_book(isbn):
    """
    Delete an existing book.
    :param isbn: unique identifier of the book
    """
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        return 'Error'
    db.session.delete(book)
    db.session.commit()


# pylint: disable=no-member
def get_book_by_isbn(isbn):
    """
    Return information about a book, isbn of the books provided in request.
    :param isbn: unique identifier of the book
    :return: Information about book in form of dict
    """
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        return book.to_dict()
    return 'Error'
