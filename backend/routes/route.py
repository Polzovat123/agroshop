from datetime import datetime
import re

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import jsonify
from flask import flash, request
from backend import app, db, bcrypt, jwt
from backend.forms.login import LoginForm
from backend.forms.registration import RegistrationForm
from backend.models.models import User


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

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not validate_input(username) or not validate_input(password):
        return jsonify({"error": "Unsuccessful validate"}), 400

    if not can_add_user(username):
        return jsonify({"error": "Not unique value"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(
                username=username,
                email=email,
                password=hashed_password,
                created_at=datetime.now(),
                updated_at=datetime.now()
                )
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return jsonify({"ok": "Successful validate"}), 200


def validate_input(input_str):
    """
    Validates user input to prevent SQL injection.
    """
    print(input_str)
    if re.search(r'[;\'"\\/]', input_str):
        return False
    return True


def can_add_user(username):
    """
    Checks if the username is available for adding a new user.
    """
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return False
    return True