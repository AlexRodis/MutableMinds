from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
    SubmitField, BooleanField, ValidationError)
from wtforms.validators import (DataRequired, 
    Length, Email, EqualTo)
from blog.models import User
from typing import Union, Optional
from blog import login_manager


@login_manager.user_loader
def load_user(user_id:int)->User:
    return User.query.get(user_id)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),Length(min=5, max=20), 
        ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(),
    ])
    password = PasswordField('Password', validators =[
        DataRequired(),
        Length(min=8, max=100),
        ])
    password_confirm = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password'),
    ])
    submit = SubmitField("Submit")

    def validate_username(self,username:StringField)->Union[ValidationError, None]:
        existing_user =  User.query.filter_by(username= username.data).first()
        if existing_user:
            raise ValidationError("Username is taken. Please try a different username.")
    
    def validate_email(self,email:StringField)->Optional[ValidationError]:
        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email:
            raise ValidationError("Email is already taken. Log in instead")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[
        DataRequired(),
        Email(),
        ])
    password = PasswordField('Password', validators=[DataRequired(),])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")