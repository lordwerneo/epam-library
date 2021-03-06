"""File with config class for application configuration."""
import os

basedir = os.path.abspath(os.path.dirname(__file__))
MIGRATION_DIR = os.path.join(basedir, 'library_app/migrations')


class Config:  # pylint: disable=too-few-public-methods
    """Config class for application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir,
                                                                  'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class TestConfig(Config):  # pylint: disable=too-few-public-methods
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://'
    WTF_CSRF_ENABLED = False
