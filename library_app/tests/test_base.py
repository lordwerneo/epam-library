import unittest
from library_app import app, db
# from library_app.models import populate_db
from config import TestConfig


class Base(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        app.config.from_object(TestConfig)
        # populate_db.populate_genre()
        # populate_db.populate_book()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
