from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Citizen(db.Model):
    __tablename__ = 'citizens'

    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    ID = db.Column(db.String(255))
    category = db.Column(db.Integer)
    status = db.Column(db.String(255))
    insurance  = db.Column(db.String(255))

    def __repr__(self):
        return f'Citizen {self.lname}'


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    company = db.Column(db.String(255))
    role = db.Column(db.String(255))
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    # pitches = db.relationship('Pitch', backref ='user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
