"""
This module defines the Base test class
"""
import unittest
from library_app import app, db
from config import TestConfig


class Base(unittest.TestCase):
    """Base test case class"""
    def setUp(self):
        """
        Execute before every test case
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        app.config.from_object(TestConfig)

    def tearDown(self):
        """
        Execute after every test case
        """
        db.session.remove()
        db.drop_all()
