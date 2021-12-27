from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, MIGRATION_DIR
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# import views
from .views import index, genres, books

# register views blueprints
app.register_blueprint(index, url_prefix='')
app.register_blueprint(genres, url_prefix='/genres')
app.register_blueprint(books, url_prefix='/books')

# import api
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

from .models import Genre, Book
