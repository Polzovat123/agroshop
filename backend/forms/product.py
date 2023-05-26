from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from backend.models.models import Users


class ProductForm(FlaskForm):
    product_id = StringField('Product id', validators=[DataRequired()])
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Product Description', validators=[DataRequired()])
    image = StringField('Product Image', validators=[DataRequired()])

