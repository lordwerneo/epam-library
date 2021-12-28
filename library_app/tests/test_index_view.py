"""
This module defines test cases for index view
"""
# pylint: disable=cyclic-import
import unittest
from library_app import app


class IndexTest(unittest.TestCase):
    """
    Class for index views test cases
    """
    def test_index(self):
        """
        Test for 200 response of index page
        """
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
