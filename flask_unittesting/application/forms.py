from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')