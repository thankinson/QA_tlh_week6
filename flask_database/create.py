from app import db
from user import User
from hobby import Hobby
from user_hobby import UserHobby
import datetime

db.drop_all()
db.create_all()

testuser1 = User(first_name='Steve', last_name='Rodgers', dob=datetime.datetime(1918,4,6), favourite_number='9')
db.session.add(testuser1)
testuser2 = User(first_name='tony', last_name='stark', dob=datetime.datetime(1918,4,6), favourite_number='9')
db.session.add(testuser2)
testuser3 = User(first_name='Peter', last_name='Parker', dob=datetime.datetime(2008,10,6), favourite_number='9')
db.session.add(testuser3)


testhobby1 = Hobby(name='Woodwork', description='lots of wood')
db.session.add(testhobby1)
testhobby2 = Hobby(name='Guitar', description='playing acdc')
db.session.add(testhobby2)

testuser_hobby1 = UserHobby(user=testuser1, hobby=testhobby1)
db.session.add(testuser_hobby1)
testuser_hobby2 = UserHobby(user=testuser2, hobby=testhobby2)
db.session.add(testuser_hobby2)
testuser_hobby3 = UserHobby(user=testuser3, hobby=testhobby2)
db.session.add(testuser_hobby3)

db.session.commit()

users = User.query.all()
hobbies = Hobby.query.all()
first_name = User.query.first()
filter_db =  Hobby.query.filter_by(name='Guitar').all()



print(users, hobbies, first_name.first_name)
print(filter_db)

get_user = User.query.get(3)
print(get_user.first_name)

user = User.query.order_by(User.first_name.desc()).first()
print(user.first_name)

first_name = User.query.first()
first_name.first_name ="Peggy"
db.session.commit()

first_name = User.query.first()
print(first_name.first_name)

