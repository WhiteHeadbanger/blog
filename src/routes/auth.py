from flask import Blueprint, jsonify, request
from flask_login import login_user, login_required, logout_user

from uuid import uuid4

# Models
from controllers.UserController import UserController

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        user = UserController.signup(data)
        return jsonify(user)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@auth.route('/login', methods = ['GET'])
def login():
    try:
        data = request.get_json()
        user = UserController.login(data)
        login_user(user, remember=True)
        return jsonify(user)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()