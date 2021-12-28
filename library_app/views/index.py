"""
This module represents the logic on / route.
"""
from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
@index.route('/index')
def index_page():
    """
    Render the index.html template on / route.
    """
    title = 'Home Page'
    return render_template('index.html', title=title)
