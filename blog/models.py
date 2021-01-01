from blog import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model,UserMixin):

    id = db.Column( db.Integer,primary_key=True,
        autoincrement=True )
    username = db.Column( db.String(25),
        unique=True, nullable=False )
    email = db.Column( db.String(125), unique=True,
        nullable=False )
    profile_pic = db.Column( db.String(20), unique=False,
        nullable=False, default='default.jpg' )
    password = db.Column(db.String(20), unique=False,
        nullable=False)
    
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.username} , {self.email}, {self.profile_pic})"


class Post(db.Model):

    
    id = db.Column( db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False , unique = True)
    date_posted = db.Column(db.DateTime, nullable=False, unique=False,
        default= datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False )


    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"

