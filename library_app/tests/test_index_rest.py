"""
This module defines test cases for index rest API
"""
import unittest
from library_app import app
from .test_base import Base


class IndexAPITest(Base):
    """
    Class for index rest API test cases
    """
    def test_index(self):
        """
        Test if /api is working, test for 200 status code
        """
        tester = app.test_client()
        response = tester.get('/api/', follow_redirects=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content_type(self):
        """
        Test if /api return correct content type
        """
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_index_data(self):
        """
        Test for correct content in response
        """
        tester = app.test_client()
        response = tester.get('/api', follow_redirects=True)
        self.assertTrue(b'resources' in response.data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
