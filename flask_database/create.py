from app import db
from user import User
import datetime

db.drop_all()
db.create_all()

testuser = User(first_name='Steve', last_name='Rodgers', dob=datetime.datetime(1918,4,6), favourite_number='9')
db.session.add(testuser)
db.session.commit()