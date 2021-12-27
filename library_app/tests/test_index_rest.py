import unittest
from library_app import app
from .test_base import Base


class IndexAPITest(Base):
    # test if /api is working
    def test_index(self):
        tester = app.test_client()
        response = tester.get('/api/', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # test if /api return correct content type
    def test_index_content_type(self):
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    # test for correct content in response
    def test_index_data(self):
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        self.assertTrue(b'resources' in response.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
