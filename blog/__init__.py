from flask import (Flask,
    render_template, url_for, flash, redirect)
from flask_sqlalchemy import SQLAlchemy
from flask_argon2 import Argon2
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '2dc1ff0736667ebe83a51cf66f44e48dfbc1759f2596174aff462b791cbce4eed997994e6c4dd8c8695470367c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
argon2 = Argon2(app,hash_len =20)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# argon2.generate_password_hash(password:str)->hashed_password:str
# argon2.check_password_hash(password_hash:str ,password:str)->checks_out:bool

from blog import urls