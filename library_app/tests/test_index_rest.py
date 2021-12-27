import unittest
from library_app import app
from .test_base import Base
from library_app.models import populate_db


class GenresTest(Base):
    # test if /api is working
    def test_index(self):
        tester = app.test_client()
        response = tester.get('/api/', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test if /api return content_type application/json
    def test_index_content_type(self):
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    # test for correct content in response
    def test_index_data(self):
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        self.assertTrue(b'links' in response.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
