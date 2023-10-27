from flask import Blueprint, jsonify, request, render_template, redirect, url_for, session
from flask_login import login_required, current_user

import traceback

# Controllers
from ..controllers.ArticleController import ArticleController

main = Blueprint('blog_blueprint', __name__)


##############################################################
# BLOG POSTS
##############################################################

@main.route('/', methods=['GET'])
def index():
    """Gets all articles and then renders index.html

    Returns:
        function: render_template('index.html')
    """
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
    """Gets one article by its ID and renders a page containing the article

    Args:
        id (str): ID representation of the article

    Returns:
        function: render_template('article.html')
    """
    try:
        article = ArticleController.get_article_by_id(id)
        return render_template('article.html', title = article.title, json_data = article.json, id = id)
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/create', methods=['GET'])
@login_required
def create():
    """Renders the create new article page

    Returns:
        function: render_template('create_article.html')
    """
    return render_template('create_article.html')

@main.route('/create', methods=['POST'])
@login_required
def create_article_post():
    """Gets json data from the new article form and creates the article

    Returns:
        function: jsonify a redirect route pointing to the recently created article
    """
    try:
        data = request.get_json()
        title = data.pop('formTitle')
        brief = data.pop('formDescription')
        uid = current_user.id
        article = ArticleController.create(uid = uid, title = title, json_data = data, brief_description = brief)
        return jsonify({'redirect': url_for('blog_blueprint.get_article_by_id', id=article.get('id'))})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/edit/<string:id>', methods=['GET'])
@login_required
def edit_article(id: str):
    """Gets one article by its ID and renders the edit article page

    Args:
        id (str): ID representation of the article

    Returns:
        function: render_template('edit_article.html') | redirect to index
    """
    article = ArticleController.get_article_by_id(id)
    if article is None:
        return redirect(url_for('blog_blueprint.index', _method='GET'))
    session["article_id"] = article.id
    return render_template('edit_article.html', article = article)

@main.route('/edit', methods=['PUT'])
@login_required
def edit_article_put():
    """Gets json data from the edited article form and modifies the article

    Returns:
        function: jsonify a redirect route pointing to the recently edited article
    """
    try:
        data = request.get_json()
        title = data.pop('formTitle')
        brief = data.pop('formDescription')
        article_id = session["article_id"]
        article = ArticleController.edit(title = title, brief_description = brief, json_data = data, article_id = article_id)
        return redirect(url_for('blog_blueprint.get_article_by_id', _method = 'GET', id = article.get('id')))
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500

@main.route('/delete', methods=['DELETE'])
@login_required
def delete_article():
    """Deletes an article

    Returns:
        function: jsonify a redirect route pointing to the recently edited article
    """
    try:
        data = request.get_json()
        requested_article = ArticleController.get_article_by_id(data.get('data'))
        article = ArticleController.delete(article_object = requested_article)
        return redirect(url_for('blog_blueprint.index', _method='GET'))
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

@main.route('/about', methods=['GET'])
def about():
    """Renders the about page

    Returns:
        function: render_template('about.html')
    """
    try:
        return render_template('about.html')
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'data':str(e)}), 500