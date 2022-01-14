"""
This module defines test cases for genre views
"""
# pylint: disable=cyclic-import
from library_app import app
from library_app.models import populate_db
from .test_base import Base


class GenresTest(Base):
    """
    Class for book views test cases
    """

    def test_genres(self):
        """
        Test /genres views with and without entries in DB
        """
        tester = app.test_client()
        response = tester.get('/genres/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        populate_db.populate_genre()
        populate_db.populate_book()
        tester = app.test_client()
        response = tester.get('/genres/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_genre(self):
        """
        Test /genre/add_genre views with get and post methods
        """
        tester = app.test_client()
        response = tester.get('/genres/add_genre', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        tester = app.test_client()
        response = tester.post('/genres/add_genre', data={
            'name': 'test',
            'description': 'test description'
        }, follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_update_genre(self):
        """
        Test /genres/update_genre/<string:genre_name> views with get and post
        methods, providing correct and incorrect infromation.
        """
        # if genre doesn't exist
        tester = app.test_client()
        response = tester.get('/genres/update_genre/fantasy')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)

        # if genre exists
        tester = app.test_client()
        populate_db.populate_genre()
        populate_db.populate_book()
        response = tester.get('/genres/update_genre/fantasy')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # if update genre
        tester = app.test_client()
        response = tester.post('/genres/update_genre/fantasy', data={
            'name': 'test',
            'description': 'test description'
        }, follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_delete_genre(self):
        """
        Test /genres/update_genre/<string:genre_name> views with get method.
        """
        # if genre doesn't exist'
        tester = app.test_client()
        response = tester.get('/genres/delete_genre/fantasy')
        statuscode = response.status_code
        self.assertEqual(statuscode, 302)
        # if genre exist
        populate_db.populate_genre()
        populate_db.populate_book()
        tester = app.test_client()
        response = tester.get('/genres/delete_genre/fantasy',
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # pylint: disable=no-member
    def test_populate(self):
        """
        Test populate /genres/populate_db
        """
        tester = app.test_client()
        response = tester.get('/genres/populate_db', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        response = tester.get('/genres/populate_db', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
