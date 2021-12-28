"""
This module defines test cases for book model
"""
import unittest
from .test_base import Base
from library_app import db
from library_app.models import Genre, Book
from library_app.models import populate_db


class BookModelCase(Base):
    """
    Class for book and genre model test cases
    """
    def test_add_genre_to_db(self):
        """
        Test insertion into genre table in DB
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        genre = Genre.query.filter_by(name='test').first()
        self.assertIsNone(genre)
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        genre = Genre.query.filter_by(name='test').first()
        self.assertEqual(genre.name, 'test')
        self.assertEqual(genre.description, 'test description')
        self.assertEqual(genre.books, [])
        self.assertNotEqual(genre.name, 'testing')
        self.assertNotEqual(genre.description, 'testing description')
        self.assertNotEqual(genre.books, [1, 2])

    def test_to_dict(self):
        """
        Test dictionary serialization of book
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        book = Book(isbn='1-23-456789-X', title='test', author='test author',
                    year=2021, publisher='test publisher', copies=5,
                    genre_id=Genre.query.filter_by(name='test').first().id)\
            .to_dict()
        self.assertEqual(book['isbn'], '1-23-456789-X')
        self.assertEqual(book['title'], 'test')
        self.assertEqual(book['author'], 'test author')
        self.assertEqual(book['year'], 2021)
        self.assertEqual(book['publisher'], 'test publisher')
        self.assertEqual(book['copies'], 5)
        self.assertEqual(book['genre'], 'test')

    def test_add_book_to_db(self):
        """
        Test insertion into book table in DB
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        book = Book.query.filter_by(isbn='1-23-456789-X').first()
        self.assertIsNone(book)
        with self.assertRaises(AttributeError):
            Book(isbn='1-23-456789-X', title='test',
                 author='test author', year=2021,
                 publisher='test publisher', copies=5,
                 genre_id=Genre.query.get(4).id)
        genre = Genre.query.get(3)
        print(genre)
        book = Book(isbn='1-23-456789-X', title='test',
                    author='test author', year=2021,
                    publisher='test publisher', copies=5,
                    genre_id=Genre.query.filter_by(name='test').first().id)
        db.session.add(book)
        db.session.commit()
        book = Book.query.filter_by(isbn='1-23-456789-X').first()
        self.assertEqual(book.isbn, '1-23-456789-X')
        self.assertEqual(book.title, 'test')
        self.assertEqual(book.author, 'test author')
        self.assertEqual(book.year, 2021)
        self.assertEqual(book.publisher, 'test publisher')
        self.assertEqual(book.copies, 5)
        self.assertEqual(book.genre_id, 3)
        self.assertNotEqual(book.isbn, '2-23-456789-X')
        self.assertNotEqual(book.title, 'testing')
        self.assertNotEqual(book.author, 'test author test')
        self.assertNotEqual(book.year, 2022)
        self.assertNotEqual(book.publisher, 'test publisher test')
        self.assertNotEqual(book.copies, 1)
        self.assertNotEqual(book.genre_id, 4)

    def test_book_repr(self):
        """
        Test book __repr__ method
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        book = Book(isbn='1-23-456789-X', title='test', author='test',
                    year=2021, publisher='test', copies=1,
                    genre_id=Genre.query.filter_by(name='fantasy').first().id)
        expected_repr = 'Book(1-23-456789-X, test, test, 2021, test, 1, 1)'
        not_expected_repr = 'Book(1-23-456789-1, test, test, 2021, test, 1, 1)'
        self.assertEqual(str(book), expected_repr)
        self.assertNotEqual(str(book), not_expected_repr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
