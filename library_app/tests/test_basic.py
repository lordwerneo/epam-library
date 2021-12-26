import unittest
from library_app import app


# class IndexTest(unittest.TestCase):
#     # Check for 200 response
#     def test_index(self):
#         tester = app.test_client(self)
#         response = tester.get('/', content_type='html/text')
#         statuscode = response.status_code
#         self.assertEqual(statuscode, 200)


if __name__ == '__main__':
    unittest.main()
