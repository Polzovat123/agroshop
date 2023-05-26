from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ChartForm(FlaskForm):
    user_id = StringField('Product id', validators=[DataRequired()])
    product_id = StringField('Product Name', validators=[DataRequired()])
    order_date = StringField('Product Description', validators=[DataRequired()])
