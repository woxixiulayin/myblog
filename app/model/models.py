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
    use_id  = db.Column(db.Integer, ForeignKey('use.id'))
    use_name = db.Column(db.String(50), ForeignKey('use.name'))
    title = db.Column(db.String(50),  unique=True)
    time_creat = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.String())
    summary = db.Column(db.String())

    comments = db.relationship('Comment')
    # user = db.relationship("User", backref=backref('blog', ))

    def __init__(self, use_id, title, content):


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    blog_id = db.Column(db.Integer, ForeignKey('blog.id'))
    use_id  = db.Column(db.Integer, ForeignKey('use.id'))
    use_name = db.Column(db.String(50),  unique=True)
    content = db.Column(db.String())
    time_creat = db.Column(db.DateTime, default=datetime.now)