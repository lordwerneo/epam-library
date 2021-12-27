import unittest
from library_app import app
from .test_base import Base
from library_app.models import populate_db, Genre
import json


class GenresAPITest(Base):
    # test if /api/genres is working
    def test_get_genres(self):
        tester = app.test_client()
        response = tester.get('/api/genres', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test if api/genres return correct content type
    def test_get_genres_content_type(self):
        tester = app.test_client()
        response = tester.get('/api/genres', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    # test for correct content in response
    def test_get_genres_data(self):
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.get('/api/genres', follow_redirects=True)
        self.assertTrue(Genre.query.get(1).name.encode() in response.data)

    # test if api/genre/fantasy is working
    def test_get_genre(self):
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.get('/api/genre/fantasy', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test if api/genres return correct content type
    def test_get_genre_content_type(self):
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.get('/api/genre/fantasy', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    # test for correct content in response
    def test_get_genre_data(self):
        # test for response if no entry in DB
        tester = app.test_client()
        response = tester.get('/api/genre/test', follow_redirects=True)
        self.assertTrue(b'No such genre' in response.data)

        # test for response if entry in DB
        populate_db.populate_genre()
        tester = app.test_client()
        response = tester.get('/api/genre/fantasy', follow_redirects=True)
        self.assertTrue(Genre.query.get(1).name.encode() in response.data)

    # test post method for genres
    def test_post_genres(self):
        # test with correct input
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'test description'
        })
        response = tester.post('/api/genres', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        data = response.data
        self.assertEqual(statuscode, 201)
        self.assertTrue(Genre.query.get(1).name.encode() in data)

        # test with empty input
        tester = app.test_client()
        payload = json.dumps({
            'name': '',
            'description': 'test description'
        })
        response = tester.post('/api/genres', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

        # test with input that already exists in DB
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'test description'
        })
        response = tester.post('/api/genres', data=payload,
                               headers={"Content-Type": "application/json"},
                               follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)

    # test put method for genres
    def test_put_genre(self):
        # test with correct input
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'test description'
        })
        response = tester.put('/api/genre/test', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        data = response.data
        self.assertEqual(statuscode, 201)
        self.assertTrue(Genre.query.get(1).name.encode() in data)

        # test with empty input
        tester = app.test_client()
        payload = json.dumps({
            'name': '',
            'description': 'test description'
        })
        response = tester.put('/api/genre/test', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

        # test with correct input to edit
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'description'
        })
        response = tester.put('/api/genre/test', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

        # test with correct input not existing entry in DB
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'description'
        })
        response = tester.put('/api/genre/fantasy', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

        # test with correct input existing entry in DB
        populate_db.populate_genre()
        tester = app.test_client()
        payload = json.dumps({
            'name': 'test',
            'description': 'description'
        })
        response = tester.put('/api/genre/fantasy', data=payload,
                              headers={"Content-Type": "application/json"},
                              follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    # test delete method for genre
    def test_delete_genre(self):
        tester = app.test_client()
        response = tester.delete('/api/genre/fantasy', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)
        populate_db.populate_genre()
        response = tester.delete('/api/genre/fantasy', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
