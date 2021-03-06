"""
This module represents the logic on /genres route.
"""
# pylint: disable=cyclic-import
from flask import Blueprint, render_template, url_for, flash, redirect
from library_app.forms import AddGenreForm, UpdateGenreForm
from library_app.service import genre_service
from library_app.models import Genre, Book, populate_db

genres = Blueprint('genres', __name__)


@genres.route('/')
def genres_page():
    """
    Renders the genres.html on /genres route.
    Show all genres.
    """
    title = 'Genres'
    genres_list = genre_service.get_all_genres()
    if genres_list == 'Error':
        genres_list = None
    return render_template('genres.html', genres_list=genres_list, title=title)


@genres.route('/add_genre', methods=['POST', 'GET'])
def add_genre():
    """
    Renders the add_genre.html on /genres/add_genre route.
    Show form to add genres.
    Redirects to /genres
    """
    form = AddGenreForm()
    if form.validate_on_submit():
        genre_service.post_genre(
            name=form.name.data.lower(),
            description=form.description.data)
        flash(f'Genre "{form.name.data}" successfully added.', 'success')
        return redirect(url_for('genres.genres_page'))
    title = 'Add Genre'
    return render_template('add_genre.html', title=title, form=form)


@genres.route('/update_genre/<string:genre_name>', methods=['POST', 'GET'])
def update_genre(genre_name):
    """
    Renders the update_genre.html on /genres/update_genre/<string:genre_name>
    route.
    Show form to update genres.
    Redirects to /genres.
    :param genre_name: name of the genre to update.
    """
    genre_to_update = Genre.query.filter_by(name=genre_name).first()
    if not genre_to_update:
        flash(f'Genre "{genre_name}" doesn\'t exist.', 'fail')
        return redirect(url_for('genres.genres_page'))
    form = UpdateGenreForm(original_name=genre_name, name=genre_to_update.name,
                           description=genre_to_update.description)
    if form.validate_on_submit():
        genre = genre_service.put_genre(current_name=genre_name,
                                        name=form.name.data,
                                        description=form.description.data)
        if genre == 'Updated':
            flash(f'Genre "{form.name.data}" successfully updated.', 'success')
            return redirect(url_for('genres.genres_page'))
    title = 'Update Genre'
    return render_template('update_genre.html', title=title, form=form)


@genres.route('/delete_genre/<string:genre_name>')
def delete_genre(genre_name):
    """
    Delete genre on /genres/delete_genre/<string:genre_name> route.
    Redirects to /genres.
    :param genre_name: name of the genre to delete.
    """
    genre_to_delete = genre_service.delete_genre(genre_name)
    if genre_to_delete == 'Error':
        flash(f'Genre "{genre_name}" does not exist.', 'fail')
        return redirect(url_for('genres.genres_page'))
    flash(f'Genre "{genre_name}" deleted.', 'warning')
    return redirect(url_for('genres.genres_page'))


# pylint: disable=no-member
@genres.route('/populate_db')
def populate():
    """
    Populate both tables in database
    """
    genres_status = Genre.query.all()
    books_status = Book.query.all()
    if not genres_status and not books_status:
        populate_db.populate_genre()
        populate_db.populate_book()
        flash('DB populated successfully', 'success')
        return redirect(url_for('genres.genres_page'))
    flash('DB population failed', 'warning')
    return redirect(url_for('genres.genres_page'))
