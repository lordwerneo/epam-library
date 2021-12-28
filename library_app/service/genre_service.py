"""
This module contains CRUD operations to work with 'genres' table.
"""
# pylint: disable=cyclic-import
from library_app import db
from ..models import Genre


# pylint: disable=no-member
def get_all_genres():
    """
    Select all records from genres table.
    :return: list of dicts of genres records in table.
    """
    genres = Genre.query.all()
    if genres:
        return [genre.to_dict() for genre in genres]
    return 'Error'


# pylint: disable=no-member
# pylint: disable=inconsistent-return-statements
def post_genre(name, description):
    """
    Add new genre to table.
    :param name: name of the genre
    :param description:  description of the genre
    """
    genre = Genre.query.filter_by(name=name).first()
    if not genre:
        genre = Genre(name=name, description=description)
        db.session.add(genre)
        db.session.commit()
        return
    return 'Error'


# pylint: disable=no-member
def put_genre(current_name, name, description):
    """
    Update an existing genre or create a new one.
    :param current_name: current name of the genre
    :param name: new name of the genre
    :param description: description of the genre
    """
    if current_name == name:
        if not Genre.query.filter_by(name=current_name).first():
            genre = Genre(name=name, description=description)
            db.session.add(genre)
            db.session.commit()
            return 'Created'
        genre = Genre.query.filter_by(name=current_name).first()
        genre.description = description
        db.session.commit()
        return 'Updated'
    if not Genre.query.filter_by(name=current_name).first():
        return 'Unknown'
    if not Genre.query.filter_by(name=name).first():
        genre = Genre.query.filter_by(name=current_name).first()
        genre.name = name
        genre.description = description
        db.session.commit()
        return 'Updated'
    return 'Busy'


# pylint: disable=no-member
# pylint: disable=inconsistent-return-statements
def delete_genre(name):
    """
    Delete an existing genre
    :param name: name of the genre
    """
    genre = Genre.query.filter_by(name=name).first()
    if not genre:
        return 'Error'
    db.session.delete(genre)
    db.session.commit()


# pylint: disable=no-member
def get_genre_by_name(name):
    """
    Return information about genre, name of the genre provided in request.
    :param name: name of the genre
    :return: Information about genre in form of dict.
    """
    genre = Genre.query.filter_by(name=name).first()
    if genre:
        return genre.to_dict()
    return 'Error'
