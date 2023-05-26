from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import jsonify, request
import os
from flask import render_template, url_for, flash, redirect, request, abort
from backend import app, db, bcrypt
from backend.forms.login import LoginForm
from backend.forms.registration import RegistrationForm
from backend.forms.product import ProductForm
from backend.models.models import Users, Product


@app.route("/")
@app.route("/home")
def home():
    return jsonify({"ok": "successful validate"}), 200


@app.route('/protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/login', methods=['POST'])
def auth_login():
    data = request.get_json()
    email = data.get('email')

    # if current_user.is_authenticated: whatt do it is question
    #     return jsonify({"error": "Invalid email or password"}), 200
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return jsonify({"error": "Unsuccessful validate"}), 400


@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    print('asd')
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        print('creat')
        # db.session.add(user)
        # db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return jsonify({"ok": "good"}), 200
    return jsonify({"error": "Unsuccessful validate"}), 400


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
            'id': product.id
        }
        return jsonify({
            "success": 1,
            "data": result
        }, 200)
    return jsonify({"error": "Unsuccessful validate"}), 400
