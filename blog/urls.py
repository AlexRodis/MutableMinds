from blog.forms import RegistrationForm, LoginForm
from flask import (render_template, url_for,
     flash, redirect, request)
from blog.models import User, Post
from blog import app,db,argon2
from flask_login import (login_user, current_user,
     logout_user, login_required)
from flask_admin.contrib.sqla import ModelView

@app.route("/")
@app.route("/home")
@app.route("/landing")
def landing():
    return render_template('index.html')



@app.route('/about')
def about():
    return 'Page Description'

@app.route('/register', 
    methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed = argon2.generate_password_hash(form.password.data)
            user = User(username=form.username.data,password=hashed,
                email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash(f'<p>Account created for {form.username.data}.</p>\
            <p>You can now log in.</p>',
                category='success')
            return redirect(url_for('landing'))
        return render_template('register.html', form = form)

@app.route('/login',
     methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and argon2.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.remember_me.data)
                next_page = request.args.get('next')      
                return redirect(next_page) if next_page else redirect(url_for('landing'))
            else:
                flash("Email or password invalid. Please enter a valid email and password")
        return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('landing'))
    else:
        logout_user()
        return redirect(url_for('landing'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/admin')
@login_required
def admin():
    return render_template()
