"""
This module contains Genre class to work with genres table
"""
# pylint: disable=cyclic-import
from library_app import db


# pylint: disable=no-member
class Genre(db.Model):
    """
    Create genres table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', cascade="all,delete",
                            backref='genre', lazy=True)

    def __repr__(self):
        """
        Representation of genre
        :return: string representing genre with name, description, books
        """
        return f'Genre({self.name}, {self.description}, {self.books})'

    def to_dict(self):
        """
        Serializer to return dictionary with genre information
        :return: dictionary of genre information
        """
        return {
            'name': self.name,
            'description': self.description,
            'unique_books': len(self.books),
            'total_copies': sum([book.copies for book in self.books])
        }
