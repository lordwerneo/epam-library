"""
This module represents the logic on /books route.
"""
# pylint: disable=cyclic-import
from flask import Blueprint, render_template, url_for, flash, redirect
from library_app.forms import AddBookForm, UpdateBookForm, FilterBookForm
from library_app.service import book_service
from library_app.models import Genre

books = Blueprint('books', __name__)


@books.route('/', methods=['POST', 'GET'])
def books_page():
    """
    Renders the books.html on /books route.
    Show all books.
    Show form to filter books by year published and genre.
    Show filtered books.
    """
    form = FilterBookForm()
    choices = [(int(genre.id), genre.name.title())
               for genre in Genre.query.all()]
    choices.insert(0, (0, ""))
    form.genre.choices = choices
    if form.validate_on_submit():
        title = 'Filtered Books'
        service = book_service.get_filtered_books
        books_list = service(year_start=form.year_start.data,
                             year_end=form.year_end.data,
                             genre=form.genre.data)
        return render_template('books.html', books_list=books_list,
                               title=title, form=form)
    service = book_service.get_all_books
    books_list = service()
    if books_list == 'Error':
        books_list = None
    title = 'Books'
    return render_template('books.html', books_list=books_list, title=title,
                           form=form)


@books.route('/add_book', methods=['POST', 'GET'])
def add_book():
    """
    Renders the add_book.html on /books/add_book route.
    Show form to add book.
    Redirects to /books
    """
    form = AddBookForm()
    choices = [(int(genre.id), genre.name.title())
               for genre in Genre.query.all()]
    form.genre.choices = choices
    if form.validate_on_submit():
        service = book_service.post_book
        service(isbn=form.isbn.data, title=form.title.data,
                author=form.author.data, year=form.year.data,
                publisher=form.publisher.data, copies=form.copies.data,
                genre=Genre.query.get(form.genre.data).name)
        flash(f'Book "{form.title.data}" successfully added.', 'success')
        return redirect(url_for('books.books_page'))
    title = 'Add Book'
    return render_template('add_book.html', title=title, form=form)


@books.route('/update_book/<string:isbn>', methods=['POST', 'GET'])
def update_book(isbn):
    """
    Renders the update_book.html on /books/update_book/<string:isbn> route.
    Show form to update books.
    Redirects go /books
    :param isbn: ISBN of the book to update.
    """
    book_to_update = book_service.get_book_by_isbn(isbn)
    if book_to_update == 'Error':
        flash(f'Book with "{isbn}" ISBN doesn\'t exist.', 'fail')
        return redirect(url_for('books.books_page'))
    form = UpdateBookForm(title=book_to_update['title'],
                          author=book_to_update['author'],
                          year=book_to_update['year'],
                          publisher=book_to_update['publisher'],
                          copies=book_to_update['copies'])
    choices = [(int(genre.id), genre.name.title())
               for genre in Genre.query.all()]
    form.genre.choices = choices
    if form.validate_on_submit():
        service = book_service.put_book
        book = service(cur_isbn=isbn, isbn=isbn, title=form.title.data,
                       author=form.author.data, year=form.year.data,
                       publisher=form.publisher.data,
                       copies=form.copies.data,
                       genre=Genre.query.get(form.genre.data).name)
        if book == 'Updated':
            flash(f'Book "{form.title.data}" successfully updated.', 'success')
            return redirect(url_for('books.books_page'))
    title = 'Update Book'
    return render_template('update_book.html', title=title, form=form)


@books.route('/delete_book/<string:isbn>')
def delete_book(isbn):
    """
    Delete book on /books/update_book/<string:isbn> route.
    Redirects to /books
    :param isbn: ISBN of the book to delete.
    """
    book_to_delete = book_service.delete_book(isbn)
    if book_to_delete == 'Error':
        flash(f'Book with "{isbn}" ISBN doesn\'t exist.', 'fail')
        return redirect(url_for('books.books_page'))
    flash(f'Book  with "{isbn}" ISBN successfully deleted.', 'warning')
    return redirect(url_for('books.books_page'))
