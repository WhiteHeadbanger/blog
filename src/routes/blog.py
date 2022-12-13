from flask import Blueprint, jsonify, request, render_template
from flask_login import login_required

import traceback

# Controllers
from controllers.PostController import PostController

main = Blueprint('blog_blueprint', __name__)


##############################################################
# BLOG POSTS
##############################################################

@main.route('/', methods=['GET'])
def index():
    try:
        posts = PostController.get_posts()
        return render_template('index.html', posts=posts)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/<string:uid>', methods=['GET'])
def get_post_by_uid(uid: str):
    try:
        posts, username = PostController.get_post_by_uid(uid)
        return render_template('posts_by_username.html', posts = posts, username = username.username)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/create', methods=['POST'])
@login_required
def create_post():
    try:
        data = request.get_json()
        post = PostController.create(post_data = data)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/edit/<string:id>', methods=['PUT'])
@login_required
def edit_post(id: str):
    try:
        data = request.get_json()
        requested_post = PostController.get_post_by_id(id)
        post = PostController.edit(post_data = data, post_obj = requested_post)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

@main.route('/delete/<string:id>', methods=['DELETE'])
@login_required
def delete_post(id: str):
    try:
        requested_post = PostController.get_post_by_id(id)
        post = PostController.delete(post_obj = requested_post)
        return jsonify(post)
    except Exception as e:
        return jsonify({'data':str(e)}), 500

##############################################################
# USER RELATED (NOT AUTH)
##############################################################

@main.route('/profile')
@login_required
def profile():
    pass

@main.route('/profile/update')
@login_required
def update_profile():
    pass

@main.route('/profile/delete')
@login_required
def delete_profile():
    pass

##############################################################
# About, Socials, etc
##############################################################

@main.route('/about')
def about():
    pass