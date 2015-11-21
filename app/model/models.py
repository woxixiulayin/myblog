from . import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50),  unique=True)
    email = db.Column(db.String(50),  unique=True)
    time_creat = db.Column(db.DateTime, default=datetime.now)

    blogs = db.relationship('Blog')
    comments = db.relationship('Comment')

    def __init__(self, name, email):
        self.name = name
        self.email = email

       
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(50) )
    title = db.Column(db.String(50),  unique=True)
    time_creat = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.String())
    summary = db.Column(db.String())

    comments = db.relationship('Comment')
    # user = db.relationship("User", backref=backref('blog', ))

    def __init__(self, user, title, content):
        self.user_id = user.id
        self.user_name = user.name
        self.title = title
        self.content = content
        self.summary = content[:50]

class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(50),  unique=True)
    content = db.Column(db.String())
    time_creat = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, user, blog, content):
        self.blog_id = blog.id
        self.user_id = user.id
        self.user_name = user.name
        self.content = content