from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length

class AddGamesForm(FlaskForm):
    name = StringField('Game Name', validators=[DataRequired(), length(min=1, max=30)])
    submit = SubmitField('Add Game')