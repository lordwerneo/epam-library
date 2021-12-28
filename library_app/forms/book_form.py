"""
This module contains web form classes to add and update book
"""
# pylint: disable=cyclic-import
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, \
    NumberRange
from library_app.models import Book
from library_app.service.book_service import isbn_checker


class AddBookForm(FlaskForm):
    """
    Form to add book to table
    """
    isbn = StringField('ISBN',
                       validators=[DataRequired(), Length(min=10, max=20)])
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=1, max=64)])
    author = StringField('Author',
                         validators=[DataRequired(), Length(min=1, max=64)])
    year = IntegerField(
        'Year',
        validators=[DataRequired(),
                    NumberRange(min=1900, max=2022,
                                message='Year should be from 1900 to 2022')])
    publisher = StringField('Publisher',
                            validators=[DataRequired(), Length(min=1, max=64)])
    copies = IntegerField(
        'Copies',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=999,
                        message='Books copies should be from 1 to 999')])
    genre = SelectField('Genre', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

    # noinspection PyMethodMayBeStatic
    # pylint: disable=no-self-use
    def validate_isbn(self, isbn):
        """
        ISBN validation function
        :param isbn: isbn of book
        :return: raise ValidationError if ISBN contains invalid information or
        already in table
        """
        isbn_db = Book.query.filter_by(isbn=isbn.data).first()
        if isbn_db:
            raise ValidationError(f'ISBN {isbn.data} already exists.')
        check_status = isbn_checker(isbn.data)
        if check_status:
            raise ValidationError(f'ISBN {isbn.data} {check_status}.')


class UpdateBookForm(FlaskForm):
    """Form to update book"""
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=1, max=64)])
    author = StringField('Author',
                         validators=[DataRequired(), Length(min=1, max=64)])
    year = IntegerField(
        'Year',
        validators=[DataRequired(),
                    NumberRange(min=1900, max=2022,
                                message='Year should be from 1900 to 2022')])
    publisher = StringField('Publisher',
                            validators=[DataRequired(), Length(min=1, max=64)])
    copies = IntegerField(
        'Copies',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=999,
                        message='Books copies should be from 1 to 999')])
    genre = SelectField('Genre', choices=[], validators=[DataRequired()])
    submit = SubmitField('Update')


class FilterBookForm(FlaskForm):
    """
    Form to filter book information for books.html
    """
    message = 'Year should be from 1900 to 2022'
    year_start = IntegerField('From', default=1900,
                              validators=[NumberRange(min=1900, max=2022,
                                                      message=message)])
    year_end = IntegerField('To', default=2022,
                            validators=[NumberRange(min=1900, max=2022,
                                                    message=message)])
    genre = SelectField('Genre', choices=[])
    submit = SubmitField('Search')
