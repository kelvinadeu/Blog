from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.model):
    __tablename__ = 'users'

    id = db.Column(db.Interger,primary_key = True)
    username = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.Column(255))
    profile_pic_path = db.Column(db.String())
    the_blog = db.relationship('Blogs',backref = 'user',lazy='dynamic')

class Single:
    def __init__(self,id,author,quotes):
        self.id=id
        self.author=author
        self.quote=quotes


class Popular:
    def __init__(self,id,name,description,url,category):
        self.id =id
        self.author =author
        self.quotes=quotes
