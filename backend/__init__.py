import os
import random

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
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

from routes.route import *
from forms import *

with app.app_context():
    for i in range(50):
        price = random.randint(1, 100) / 100
        product = Product(
            product_name='продукт №' + str(i),
            description='это продукт №' + str(i),
            type_id=0,
            tags_id=0,
            date_of_publication=datetime.now(),
            date_update=datetime.now(),
            image= f"asdfasd{i}",
            price=price,
            old_price=int(price * 1.3) if random.randint(0, 1) > 0 else price
        )
        db.session.add(product)
        db.session.commit()
    db.create_all()

