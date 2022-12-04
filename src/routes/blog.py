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
def get_post_by_uid(uid: str):
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

@main.route('/edit/<string:id>', methods=['PUT'])
def edit_post(id: str):
    try:
        data = request.get_json()
        requested_post = PostController.get_post_by_id(id)
        post = PostController.edit(post_data = data, post_obj = requested_post)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/delete/<string:id>', methods=['DELETE'])
def delete_post(id: str):
    try:
        requested_post = PostController.get_post_by_id(id)
        post = PostController.delete(post_obj = requested_post)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500



