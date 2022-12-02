from flask import Blueprint, jsonify, request

from uuid import uuid4

# Models
from models.UserModel import UserModel

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():
    try:
        pass
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@auth.route('/login', methods = ['GET'])
def login():
    try:
        pass
    
    except Exception as e:
        return jsonify({'data':str(e)}), 500