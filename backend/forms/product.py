from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    product_id = StringField('Product id', validators=[DataRequired()])
    product_name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Product Description', validators=[DataRequired()])
    image = StringField('Product Image', validators=[DataRequired()])

