"""File with config class for application configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:   # pylint: disable=too-few-public-methods
    """Config class for application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG = 1
