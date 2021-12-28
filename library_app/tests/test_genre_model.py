"""
This module defines the test cases for genre model
"""
import unittest
from .test_base import Base
from library_app import app, db
from library_app.models import Genre


class GenreModelCase(Base):
    """Class for genre model test cases"""
    def setUp(self):
        """
        Execute before each test case
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        """
        Execute after each test case
        """
        db.session.remove()
        db.drop_all()

    def test_to_dict(self):
        """
        Test dictionary serialization of genre
        """
        genre = Genre(name='test', description='test description').to_dict()
        self.assertEqual(genre['name'], 'test')
        self.assertEqual(genre['description'], 'test description')
        self.assertEqual(genre['unique_books'], 0)
        self.assertEqual(genre['total_copies'], 0)

    def test_genre_repr(self):
        """
        Test genre __repr__ method
        """
        genre = Genre(name='Test', description='Test description.')
        self.assertEqual(str(genre), 'Genre(Test, Test description., [])')
        self.assertNotEqual(str(genre), 'Genre(Test, Test description., {})')


if __name__ == '__main__':
    unittest.main(verbosity=2)
