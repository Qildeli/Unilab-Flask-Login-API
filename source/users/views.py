from flask import render_template, url_for, flash, redirect, Blueprint
from source import db, bcrypt
from source.users.forms import LoginForm, RegistrationForm
from source.models import User
from flask_login import login_user, logout_user, current_user, login_required

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You have registered successfully', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', title='Sign up', form=form)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Log In', form=form)


@users_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users_blueprint.route("/account")
@login_required
def account():
    return render_template('account.html', title='You are logged in')
