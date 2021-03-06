"""
This module defines test case for book service
"""
# pylint: disable=cyclic-import
import unittest
from library_app.service.book_service import isbn_checker


class TestBookService(unittest.TestCase):
    """
    Class for book service test
    """
    def test_isbn_checker(self):
        """
        Testing isbn_checker function.
        It should return results from isbn_cases[1], based in isbn_cases[0]
        input.
        """
        isbn_cases = [
            ['978-1-60309-025-4', None],
            ['0-7475-3269-9', None],
            ['978-1-933624-34-1', None],
            ['1-23-456789-X', None],
            ['978-1-60309-025-X', 'Invalid length'],
            ['978-1-60309-02-5-4', 'Invalid format'],
            ['978-1-60309-025-3', 'Invalid checksum'],
            ['978-1-60309-0Z5-4', 'Invalid characters'],
            ['978-1-60309+025-4', 'Invalid characters'],
            ['1-23-456789-1', 'Invalid checksum'],
            ['1-23-A56789-X', 'Invalid characters'],
            ['1-23-4-56789-X', 'Invalid length']]
        for case in isbn_cases:
            result = isbn_checker(case[0])
            self.assertEqual(result, case[1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
