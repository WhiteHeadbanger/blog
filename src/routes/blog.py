from flask import Blueprint, jsonify, request
from uuid import uuid4

# Controllers
from controllers.PostController import PostController

main = Blueprint('blog_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_posts():
    try:
        posts = PostController.get_posts()
        return jsonify(posts)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/<string:uid>', methods=['GET'])
def get_post_by_uid(uid: int):
    try:
        posts = PostController.get_post_by_uid(uid)
        return jsonify(posts)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/create', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        post = PostController.create(post_data = data)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/edit', methods=['POST'])
def edit_post():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/delete', methods=['POST'])
def delete_post():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'data':str(e)}), 500



