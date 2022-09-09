from flask import Flask, request, render_template
from application import db
from application import app
from application.models import Register
from application.forms import RegisterForm

@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        person = Register(name=form.name.data)
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)
