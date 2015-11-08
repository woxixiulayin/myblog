from . import db
from datetime import datetime



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),  unique=True)
	time_creat = db.Column(db.DateTime, default=datetime.now)

	def __init__(self, name=None):
		self.name = name
	def __repr__(self):
	    return '<User %r>' % (self.name)