"""
This module contains web form classes to add and update genre
"""
# pylint: disable=cyclic-import
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from library_app.models import Genre


class AddGenreForm(FlaskForm):
    """
    Form to add genre to table
    """
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=1, max=20)])
    description = StringField('Description',
                              validators=[DataRequired(),
                                          Length(min=1, max=255)])
    submit = SubmitField('Submit')

    # noinspection PyMethodMayBeStatic
    # pylint: disable=no-self-use
    def validate_name(self, name):
        """
        Name validation function
        :param name: name of genre
        :return: raise ValidationError if name contains invalid information or
        already in table
        """
        name_db = Genre.query.filter_by(name=name.data.lower()).first()
        if name_db:
            raise ValidationError(f'Genre "{name.data}" already exists.')
        if not name.data.isalpha():
            raise ValidationError('Genre should contain only letters.')


class UpdateGenreForm(AddGenreForm):
    """Form to update genre"""
    submit = SubmitField('Update')

    def __init__(self, original_name, *args, **kwargs):
        """
        Initialization to create original_name variable to check name before
        updating entry in table
        """
        super().__init__(*args, **kwargs)
        self.original_name = original_name

    # noinspection PyMethodMayBeStatic
    # pylint: disable=no-self-use
    def validate_name(self, name):
        """
        Name validation function
        :param name: name of genre
        :return: raise ValidationError if name contains invalid information or
        already in table
        """
        name_db = Genre.query.filter_by(name=name.data.lower()).first()
        if name_db and name.data != self.original_name:
            raise ValidationError(f'Genre "{name.data}" already exists.')
        if not name.data.isalpha():
            raise ValidationError('Genre should contain only letters.')
