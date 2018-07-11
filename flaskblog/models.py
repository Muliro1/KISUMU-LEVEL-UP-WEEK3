from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True) 
	username = db.Column(db.String(20), unique=True)
	email = db.Column(db.String(120), unique=True)
	image_file = db.Column(db.String(20),default='default.jpg')
	password = db.Column(db.String(60))
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return 'User {} {} {}'.format(self.username, self.email, self.image_file)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	date_posted = db.Column(db.DateTime, default=datetime.utcnow())
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return 'User {} {}'.format(self.title, self.date_posted)