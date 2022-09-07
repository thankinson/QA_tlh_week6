from email import message
from flask import Flask, request, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from decimal import ROUND_HALF_UP

app = Flask(__name__)
app.config['SECRET_KEY']='bew_ldJsjOWMQvGqF50ebw'

@app.route('/')
def index():
    return render_template('index.html')

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = "Please enter another user name"
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)


class UserInfo(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20), UserCheck(message="The user Name is not allowed", banned=['root', 'admin', 'sys'])])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=20)])
    dob = DateField('Date Of Birth')
    favourite_number = DecimalField('Favourite Number', places = 2, rounding=ROUND_HALF_UP)
    favourite_food = SelectField('Favourite Food', choices=[('USA', 'fried-chicken'), ('ITY', 'spaghetti'), ('MEX', 'chilli')])
    submit = SubmitField('Add User')

@app.route('/adduser', methods = ['GET', 'POST'])
def add_user():
    message = ""
    add_user_form = UserInfo()

    if request.method == 'POST':
        if add_user_form.validate_on_submit():
            first_name = add_user_form.first_name.data
            last_name = add_user_form.last_name.data
            dob = add_user_form.dob.data
            favourite_number = add_user_form.favourite_number.data
            favourite_food = add_user_form.favourite_food.data

        message = f'First name: {first_name}, Last Name: {last_name}, DOB: {dob}, Favourite Number: {favourite_number}, Favourite Food: {favourite_food}'

    return render_template('adduser.html', form=add_user_form, message=message)

class UserLogin(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_login = UserLogin()
    return render_template('login.html', form=user_login)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)