"""
This module contains Book class to work with books table
"""
# pylint: disable=cyclic-import
from library_app import db
from library_app.models.genre import Genre


# pylint: disable=no-member
class Book(db.Model):
    """
    Create books table
    """
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(64), nullable=False)
    copies = db.Column(db.Integer, nullable=False, default=1)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    def __repr__(self):
        """
        Representation of book
        :return: string representing book including all the information
        """
        return f'Book({self.isbn}, {self.title}, {self.author}, ' \
               f'{self.year}, {self.publisher}, {self.copies}, ' \
               f'{self.genre_id})'

    def to_dict(self):
        """
        Serializer to return dictionary with book infomration
        :return: dictionary of book infomration
        """
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'publisher': self.publisher,
            'copies': self.copies,
            'genre': Genre.query.get(self.genre_id).name
        }
