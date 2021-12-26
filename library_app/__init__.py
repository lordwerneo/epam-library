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
