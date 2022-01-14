"""
__init__.py file of library_app module.
Import all the necessary modules and sub-folders.
Define all the needed variables for the application.
Register all API resources.
Register all the blueprints.
"""
# pylint: disable=cyclic-import
import logging
import sys
from logging.handlers import RotatingFileHandler
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config, MIGRATION_DIR


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# file handler for Logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
LOG_PATH = 'library.log'
file_handler = RotatingFileHandler(LOG_PATH, maxBytes=102400,
                                   backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)

# pylint: disable=no-member
logger = app.logger
logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)
logger.info('Library app starting')


# import views
# pylint: disable=cyclic-import
# pylint: disable=wrong-import-position
from .views import index, genres, books

# register views blueprints
app.register_blueprint(index, url_prefix='')
app.register_blueprint(genres, url_prefix='/genres')
app.register_blueprint(books, url_prefix='/books')

# import api
# pylint: disable=cyclic-import
# pylint: disable=wrong-import-position
from .rest import Index, GenresList, GenresSolo, BooksGenreList, BooksList, \
    BooksSolo

# register api blueprints
api.add_resource(Index, '/')
api.add_resource(GenresList, '/genres')
api.add_resource(GenresSolo, '/genre/<string:name>')
api.add_resource(BooksList, '/books')
api.add_resource(BooksGenreList, '/books/<string:genre>')
api.add_resource(BooksSolo, '/book/<string:isbn>')
app.register_blueprint(api_bp, url_prefix='/api')

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# import models
# pylint: disable=cyclic-import
# pylint: disable=wrong-import-position
from .models import Genre, Book
