from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

# Controllers
from ..controllers.UserController import UserController

auth = Blueprint('auth', __name__)

'''
@auth.route('/signup', methods=['GET'])
def signup():
    """Renders the sign up page

    Returns:
        function: render_template('signup.html')
    """
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    """Creates the user and redirects to the login page

    Returns:
        function: redirect to the login page (route)
    """
    try:
        data = request.form
        user = UserController.signup(data)
        return redirect(url_for('auth.login'))
    except Exception as e:
        error_message = str(e)
        flash(error_message, category="error")
        return render_template('signup.html', error=error_message), 500
'''
        
@auth.route('/login', methods = ['GET'])
def login():
    """Renders the login page

    Returns:
        function: render_template('login.html')
    """
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login_post():
    """Gets the user data and makes a login

    Returns:
        function: redirect to the index page (route)
    """
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
    """Logs out user

    Returns:
        function: redirect to the index page (route)
    """
    logout_user()
    return redirect(url_for('blog_blueprint.index'))