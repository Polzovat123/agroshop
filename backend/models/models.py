from sqlalchemy.dialects.postgresql import JSON
from backend import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    shop_rating = db.Column(db.Integer(), nullable=False)
    is_farmer = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)  # TODO TIMESTAMP
    farmer_rating = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<Farmer %r>' % self.farmer_name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)