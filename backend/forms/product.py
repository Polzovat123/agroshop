from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from backend.models.models import Client


class ProductForm(FlaskForm):
    product_id = StringField('Product id', validators=[DataRequired()])
