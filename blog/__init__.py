from flask import (Flask,
    render_template, url_for, flash, redirect)
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = '2dc1ff0736667ebe83a51cf66f44e48dfbc1759f2596174aff462b791cbce4eed997994e6c4dd8c8695470367c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

db = SQLAlchemy(app)
argon2 = Argon2(app,hash_len =20)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


class BlogModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self,name,**kwargs):
        return redirect(url_for('login',next=request.url))


from blog.models import User, Post
admin = Admin(app, name='Mutable Minds', template_mode='bootstrap3')
admin.add_view(BlogModelView(User,db.session))
admin.add_view(BlogModelView(Post,db.session))


# argon2.generate_password_hash(password:str)->hashed_password:str
# argon2.check_password_hash(password_hash:str ,password:str)->checks_out:bool

from blog import urls