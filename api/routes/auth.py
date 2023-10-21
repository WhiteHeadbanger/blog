from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from uuid import uuid4

# Controllers
from ..controllers.UserController import UserController

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    try:
        data = request.form
        user = UserController.signup(data)
        return redirect(url_for('auth.login'))
    except Exception as e:
        error_message = str(e)
        flash(error_message, category="error")
        return render_template('signup.html', error=error_message), 500

@auth.route('/login', methods = ['GET'])
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login_post():
    try:
        data = request.form
        remember = True if request.form.get('rememberme') else False
        user = UserController.login(data)
        login_user(user, remember=remember)
        return redirect(url_for('blog_blueprint.index'))
    except Exception as e:
        error_message = str(e)
        flash(error_message, category="error")
        return render_template('login.html'), 500

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog_blueprint.index'))