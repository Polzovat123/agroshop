from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token
from flask import jsonify, request
import os
from flask import render_template, url_for, flash, redirect, request, abort
from backend import app, db, bcrypt
from backend.forms.login import LoginForm
from backend.forms.registration import RegistrationForm
from backend.models.models import User


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
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            access_token = create_access_token(identity=email)
            return jsonify(access_token=access_token), 200
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return jsonify({"error": "Unsuccessful validate"}), 400


@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return
