from flask import Flask
#from flask import Blueprint 
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
migrate = Migrate(app, db)


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     db.init_app(app)
#     migrate = Migrate()

#     with app.app_context():

from .import routes, models








#from .import routes, models

# bp = Blueprint('api', __name__ url_prefix='/api)
# app = Flask(__name__)


