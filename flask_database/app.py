from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
# from app import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)

# db.create_all()

if __name__=='__main__':
    app.run(debug=True)