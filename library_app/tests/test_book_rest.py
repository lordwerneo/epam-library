"""
This module defines test cases for book rest API
"""
import unittest
import json
from library_app import app
from library_app.models import populate_db, Book
from .test_base import Base


class BooksAPItest(Base):
    """
    Class for book rest API test cases
    """
    def test_get_books(self):
        """
        Test if /api/books is working with empty db
        """
        tester = app.test_client()
        response = tester.get('/api/books', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_books_content_type(self):
        """
        Test if /api/books return correct content type
        """
        tester = app.test_client()
        response = tester.get('/api/books', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_books_data(self):
        """
        Test for correct content in response
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        tester = app.test_client()
        response = tester.get('/api/books', follow_redirects=True)
        self.assertTrue(Book.query.get(1).isbn.encode() in response.data)

    def test_get_book(self):
        """
        Test if api/book/0-7475-3269-9 is working
        """
        populate_db.populate_genre()
        populate_db.populate_book()
        tester = app.test_client()
        response = tester.get('api/book/0-7475-3269-9', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_genre_content_type(self):
        """
        Test if api/book/0-7475-3269-9 return correct content type
        """
        tester = app.test_client()
        response = tester.get('api/book/0-7475-3269-9', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_get_book_data(self):
        """
        Test for correct response for api/book/0-7475-3269-9
        """
        # test for response if no entry in DB
        tester = app.test_client()
        response = tester.get('api/book/0-7475-3269-9', follow_redirects=True)
        self.assertTrue(b'No such book' in response.data)

        # test for response if entry in DB
        populate_db.populate_genre()
        populate_db.populate_book()
        response = tester.get('api/book/0-7475-3269-9', follow_redirects=True)
        self.assertTrue(Book.query.get(1).isbn.encode() in response.data)

    def test_get_books_by_genre(self):
        """
        Test for correct response for books sorted by genre
        """
        # if genre doesn't exist
        tester = app.test_client()
        response = tester.get('api/books/fantasy', follow_redirects=True)
        self.assertTrue(b'No fantasy genre' in response.data)

        # if genre has no books
        populate_db.populate_genre()
        response = tester.get('api/books/fantasy', follow_redirects=True)
        self.assertTrue(b'No books in fantasy' in response.data)

        # if genre exists and book in genre
        populate_db.populate_book()
        response = tester.get('api/books/fantasy', follow_redirects=True)
        self.assertTrue(Book.query.get(1).isbn.encode() in response.data)

    def test_post_books(self):
        """
        Test post method for books
        """
        # test data validator with incorrect data
        tester = app.test_client()
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1801,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "test"})
        response = tester.post('api/books', data=payload,
                               headers={'Content-type': 'application/json'},
                               follow_redirects=True)
        self.assertTrue(b'Wrong data input' in response.data)

        # test with correct data but no genre entry in DB
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "test"})
        response = tester.post('api/books', data=payload,
                               headers={'Content-type': 'application/json'},
                               follow_redirects=True)
        self.assertTrue(b'Genre test not found' in response.data)

        # test with correct data
        populate_db.populate_genre()
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "fantasy"})
        response = tester.post('api/books', data=payload,
                               headers={'Content-type': 'application/json'},
                               follow_redirects=True)
        self.assertTrue(b'/api/book/1-23-456789-X' in response.data)

        # test with correct data but busy ISBN entry
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "fantasy"})
        response = tester.post('api/books', data=payload,
                               headers={'Content-type': 'application/json'},
                               follow_redirects=True)
        self.assertTrue(b'Book 1-23-456789-X already exists' in response.data)

    def test_put_book(self):
        """
        Test put method for book
        """
        # test data validator with incorrect data
        tester = app.test_client()
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1801,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "test"})
        response = tester.put('api/book/1-23-456789-X', data=payload,
                              headers={'Content-type': 'application/json'},
                              follow_redirects=True)
        self.assertTrue(b'Wrong data input' in response.data)

        # test with correct data but no genre entry in DB
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "test"})
        response = tester.put('api/book/1-23-456789-X', data=payload,
                              headers={'Content-type': 'application/json'},
                              follow_redirects=True)
        self.assertTrue(b'Genre test not found' in response.data)

        # test with correct data to update entry with busy ISBN
        populate_db.populate_genre()
        populate_db.populate_book()
        payload = json.dumps({"isbn": "0-7475-3269-9",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "fantasy"})
        response = tester.put('api/book/1-23-456789-X', data=payload,
                              headers={'Content-type': 'application/json'},
                              follow_redirects=True)
        self.assertTrue(b'Book 0-7475-3269-9 already exists' in response.data)

        # test with correct data to put new entry in DB
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "test title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "fantasy"})
        response = tester.put('api/book/1-23-456789-X', data=payload,
                              headers={'Content-type': 'application/json'},
                              follow_redirects=True)
        self.assertFalse(b'Book 1-23-456789-X updated' in response.data)
        self.assertTrue(b'api/book/1-23-456789-X' in response.data)

        # test with correct data to update existing entry in DB
        payload = json.dumps({"isbn": "1-23-456789-X",
                              "title": "new title",
                              "author": "test author",
                              "year": 1901,
                              "publisher": "test publisher",
                              "copies": 1,
                              "genre": "fantasy"})
        response = tester.put('api/book/1-23-456789-X', data=payload,
                              headers={'Content-type': 'application/json'},
                              follow_redirects=True)
        self.assertTrue(b'Book 1-23-456789-X updated' in response.data)

    def test_delete_book(self):
        """Test delete method for book with"""
        # test deletion of not existing entry
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.delete('api/book/0-7475-3269-9',
                                 headers={'Content-type': 'application/json'},
                                 follow_redirects=True)
        self.assertTrue(b'No such book' in response.data)

        # test deletion of existing entry
        populate_db.populate_book()
        response = tester.delete('api/book/0-7475-3269-9',
                                 headers={'Content-type': 'application/json'},
                                 follow_redirects=True)
        self.assertTrue(b'Book 0-7475-3269-9 deleted' in response.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
