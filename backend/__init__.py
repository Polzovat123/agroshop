import os
import random

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', '5791628bb0b13ce0c676dfde280ba245')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('FLASK_DB_URL', 'sqlite:///../database/sqlite.db')
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)
db.app = app
jwt = JWTManager(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

from backend.routes.route import *
from backend.forms import *

with app.app_context():
    db.create_all()
