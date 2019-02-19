from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    the_blog = db.relationship('Blogs',backref = 'user',lazy='dynamic')
    comment = db.relationship('comment',backref='user',lazy='dynamic')

    @property
    def password(self):
         raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'{self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

class Blogs():
    blog_list=[]
    __tablename__='blogs'
    # id = db.Column(db.,primary_key=True)
    post = db.Column(db.String(255),index = True)
    title = db.Column(db.String(255),index = True)
    Posted = db.Column(db.DateTime,default = datetime.utcnow)
    # user_id = db.Column(db.Interger,db.ForeignKey('users.id'))
    comments = db.ForeignKey('comment',lazy = 'dynamic')

    def __init__(self,title,post,user):
        self.user =user
        self.title = title
        self.post = post

    def save_blogs(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        blogs = Blogs.query.all()
        return blogs

    @classmethod
    def delete_all_blogs(cls):
        Blogs.all_blog.delete()

class Comment():
    comments_list=[]
    __tablename__='comments'

    # id = db.Column(db.Interger,primary_key =True)
    name = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),index= True)
    # blog_id = db.Column(db.Interger,db.ForeignKey('blog_id'))
    commenter_id = db.Column(db.String(255),index = True)
    posted = db.Column(db.DateTime,default = datetime.utcnow)

    def __init__(self,name,comment_itself,blog):
        self.name = name
        self.comment_itself = comment_itself
        self.blog = blog

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments

    @classmethod
    def delete_all_blogs(cls):
        Blogs.all_blogs.delete()


class Random:
    def __init__(self,id,author,quote):
        self.id=id
        self.author=author
        self.quote=quote
