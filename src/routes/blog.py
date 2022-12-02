from flask import Blueprint, jsonify, request
from uuid import uuid4

# Controllers
from controllers.PostController import PostController

main = Blueprint('blog_blueprint', __name__)

@main.route('/')
def get_posts():
    try:
        posts = PostController.get_posts()
        return jsonify(posts)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/create', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'data':str(e)}), 500



