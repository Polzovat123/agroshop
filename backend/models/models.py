from sqlalchemy.dialects.postgresql import JSON
from backend import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)
    age = db.Column(db.Integer(), nullable=True)
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


class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)  # TODO TIMESTAMP
    farmer_rating = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<nickname %r>' % self.nickname


class Product(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    type_id = db.Column(db.Integer(), nullable=False)
    tags_id = db.Column(db.Integer(), nullable=False)
    date_of_publication = db.Column(db.DateTime, nullable=False)
    date_update = db.Column(db.DateTime, nullable=False)  # TODO TIMESTAMP
    image = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    old_price = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<product_name %r>' % self.product_name


class ProductTagRelationship(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_id = db.Column(db.Integer(), nullable=False)
    tag_id = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id


class ShoppingCartProductRelationship(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    shopping_cart_id = db.Column(db.Integer(), nullable=False)
    product_id = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id


class ProductTag(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    nametag = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<nametag %r>' % self.nametag


class ProductType(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_type = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id




