from datetime import datetime
import re

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import jsonify
from flask import flash, request
from backend import app, db, bcrypt, jwt
from backend.forms.login import LoginForm
from backend.forms.registration import RegistrationForm
from backend.forms.product import ProductForm
from backend.models.models import Users, Product


@app.route("/")
@app.route("/home")
def home():
    db.create_all()
    return jsonify({"ok": "successful validate"}), 200


@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not validate_input(username) or not validate_input(password):
        return jsonify({"error": "Unsuccessful validate"}), 400

    user = Users.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    age = data.get('age')
    is_farmer = data.get('is_farmer')

    if not validate_input(username) or not validate_input(password):
        return jsonify({"error": "Unsuccessful validate"}), 400

    if not can_add_user(username):
        return jsonify({"error": "Not unique value"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = Users(
                username=username,
                email=email,
                password=hashed_password,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                age=age,
                shop_rating=50,
                is_farmer=is_farmer
                )
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return jsonify({"ok": "Successful validate"}), 200


def validate_input(input_str):
    """
    Validates user input to prevent SQL injection.
    """
    if re.search(r'[;\'"\\/]', input_str):
        return False
    return True


def can_add_user(username):
    """
    Checks if the username is available for adding a new user.
    """
    existing_user = Users.query.filter_by(username=username).first()
    if existing_user:
        return False
    return True


@app.route('/products', methods=['GET'])
def get_products():
    items_on_page_count = 10
    price = request.args.get('price', default='asc', type=str)
    current_page = request.args.get('page', default=1, type=int)

    if price == 'asc':
        order = Product.price.asc()
    else:
        order = Product.price.desc()
    products = Product.query.order_by(order).all()

    total_pages = len(products) % 10
    if current_page > total_pages:
        return jsonify({"error": "Page not found"}), 404

    products = products[(current_page - 1) * items_on_page_count:current_page * items_on_page_count]
    result = []
    for product in products:
        result.append({
            'id': product.id,
            'product_name': product.product_name,
            'description': product.description,
            'image': product.image,
        })
    return jsonify({
        "success": 1,
        "data": result,
        "total_pages": total_pages
    }, 200)


@app.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(product_id: int):
    product = Product.get(Product.id == product_id)
    if product:
        result = {
            'id': product.id,
            'product_name': product.product_name,
            'description': product.description,
            'image': product.image,
        }
        return jsonify({
            "success": 1,
            "data": result
        }, 200)
    return jsonify({"error": "Unsuccessful validate"}), 400


@app.route('/create_product', methods=['POST'])
def create_product():
    data = request.get_json()
    product_name = data.get('product_name')
    description = data.get('description')
    image = data.get('image')

    if not validate_input(product_name) or not validate_input(description):
        return jsonify({"error": "Unsuccessful validate"}), 400

    product = Product(
        product_name=product_name,
        description=description,
        type_id=0,
        tags_id=0,
        date_of_publication=datetime.now(),
        date_update=datetime.now(),
        image=image,
        price=0,
        old_price=0
    )

    db.session.add(product)
    db.session.commit()
    return jsonify({'ok': 'created successfully'}), 200


@app.route('/delete_product', methods=['GET'])
def delete_product():
    data = request.json()
    product = Product.get(Product.id == data["id"])

    db.session.delete(product)
    db.session.commit()

    return jsonify({'ok', 'deleted complete'}), 201


@app.route('/update_product', methods=['POST'])
def update_product():
    data = request.json()
    product = Product.query.filter_by(id=data["id"]).first()
    if product:
        product.product_name = data["product_name"]
        product.description = data["description"]
        product.image = data["image"]
        product.price = data["price"]
        product.old_price = data["old_price"]
        db.session.commit()
        return jsonify({'ok', 'updated complete'}), 201
    else:
        return jsonify({'Not', 'product not found'}), 404
