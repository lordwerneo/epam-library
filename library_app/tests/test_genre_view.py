import unittest
from library_app import app
from .test_base import Base
from library_app.models import populate_db


class GenresTest(Base):
    def test_genres(self):
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


if __name__ == '__main__':
    unittest.main()
