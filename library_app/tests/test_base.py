"""
This module defines the Base test class
"""
import unittest
from config import TestConfig
from library_app import app, db


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
