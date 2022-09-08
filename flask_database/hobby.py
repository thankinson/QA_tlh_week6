from app import db

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(), nullable=True)
    hobby_users = db.relationship('UserHobby', backref='hobby')