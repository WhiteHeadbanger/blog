from flask import Blueprint, jsonify, request, render_template, redirect, url_for, Response, session
from flask_login import login_required, current_user

import traceback

# Controllers
from controllers.ArticleController import ArticleController

main = Blueprint('blog_blueprint', __name__)


##############################################################
# BLOG POSTS
##############################################################

@main.route('/', methods=['GET'])
def index():
    try:
        articles = ArticleController.get_articles()
        return render_template('index.html', articles = articles)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/editor-articles/<string:uid>', methods=['GET'])
def get_article_by_uid(uid: str):
    try:
        articles, username = ArticleController.get_article_by_uid(uid)
        return render_template('articles_by_username.html', articles = articles, username = username.username)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/article/<string:id>', methods=['GET'])
def get_article_by_id(id: str):
    try:
        article = ArticleController.get_article_by_id(id)
        return render_template('article.html', title = article.title, json_data = article.json)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/create', methods=['GET'])
@login_required
def create():
    return render_template('create_article.html')

@main.route('/create', methods=['POST'])
@login_required
def create_article_post():
    try:
        data = session["new_article_data"]
        title = request.form.get("article-title")
        brief = request.form.get("brief-description")
        uid = current_user.id
        article = ArticleController.create(uid = uid, title = title, json_data = data, brief_description = brief)
        return redirect(url_for('blog_blueprint.index'))
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/fetch-data', methods=['POST'])
@login_required
def fetch_new_article_data():
    try:
        data = request.get_json()
        session["new_article_data"] = ""
        session["new_article_data"] = data
        return redirect(url_for('blog_blueprint.create_article_post'))
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/edit/<string:id>', methods=['PUT'])
@login_required
def edit_article(id: str):
    try:
        data = request.get_json()
        requested_article = ArticleController.get_article_by_id(id)
        article = ArticleController.edit(article_data = data, article_obj = requested_article)
        return jsonify(article)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/delete/<string:id>', methods=['DELETE'])
@login_required
def delete_article(id: str):
    try:
        requested_article = ArticleController.get_article_by_id(id)
        article = ArticleController.delete(article_obj = requested_article)
        return jsonify(article)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500
    

##############################################################
# USER RELATED (NOT AUTH)
##############################################################

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

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