"""
This module defines test cases for book views
"""
# pylint: disable=cyclic-import
import unittest
from library_app import app
from library_app.models import populate_db
from .test_base import Base


class BookTest(Base):
    """
    Class for book views test cases
    """
    def test_books(self):
        """
        Test /books view with and without filter
        """
        # test view without filter
        populate_db.populate_genre()
        populate_db.populate_book()
        tester = app.test_client()
        response = tester.get('/books', content_type='html/text',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        # test view with filter
        tester = app.test_client()
        response = tester.post('/books/', data={'year_start': 1900,
                                                'year_end': 2022,
                                                'genre': 1},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_book(self):
        """
        Test /books/add_book views with get and post methods.
        """
        # test add book view with get method
        tester = app.test_client()
        response = tester.get('/books/add_book')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test add book view with post method
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.post('/books/add_book',
                               data={'isbn': '1-23-456789-X',
                                     'title': 'test title',
                                     'author': 'test author',
                                     'year': 1999,
                                     'publisher': 'test publisher',
                                     'copies': 1,
                                     'genre': 1},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_book(self):
        """
        Test /books/update_book/<string:book_isbn> views with get and post
        methods, providing correct and incorrect information.
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        # test update book providing wrong isbn with get method
        tester = app.test_client()
        response = tester.get('/books/update_book/test',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test update book providing correct isbn with get method
        tester = app.test_client()
        response = tester.get('/books/update_book/0-7475-3269-9',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test update book providing correct isbn with post method
        tester = app.test_client()
        response = tester.post('/books/update_book/0-7475-3269-9',
                               data={'title': 'test title',
                                     'author': 'test author',
                                     'year': 1999,
                                     'publisher': 'test publisher',
                                     'copies': 1,
                                     'genre': 1},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_book(self):
        """
        Test /books/delete_book/<string:book_isbn> views with get method.
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        # test delete book with correct isbn
        tester = app.test_client()
        response = tester.get('/books/delete_book/0-7475-3269-9',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test delete book with correct isbn that was already deleted
        tester = app.test_client()
        response = tester.get('/books/delete_book/0-7475-3269-9',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


# pylint: disable=duplicate-code
if __name__ == '__main__':
    unittest.main(verbosity=2)
