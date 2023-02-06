from . import ArticleModel as am
from . import UserModel as um
from uuid import uuid4
from database.db import db

def get_articles():
    return am.ArticleModel.query.all()

def get_article_by_id(id: str):
    return am.ArticleModel.query.filter_by(id = id).one()

def get_article_by_uid(uid: str):
    return am.ArticleModel.query.filter_by(uid = uid).all()

def create_article(uid: str, title: str, html_data: str):
    new_article = am.ArticleModel(
        id = str(uuid4()),
        uid = uid,
        title = title,
        html_data = html_data
    )
    
    db.session.add(new_article)
    db.session.commit() 

    return new_article.serialize()

def edit_article(article_obj: am.ArticleModel, title: str = None, body: str = None):
    article_obj.title = title
    article_obj.body = body
    db.session.commit()

    return article_obj.serialize()

def delete_article(article_obj: am.ArticleModel):
    article = article_obj.serialize()
    db.session.delete(article_obj)
    db.session.commit()

    return article

def get_users():
    pass

def get_user_by_username(username: str):
    return um.UserModel.query.filter_by(username = username).first()

def get_user_by_uid(uid: str):
    return um.UserModel.query.filter_by(id = uid).first()

def create_user(username: str, password: str):
    new_user = um.UserModel(
        id = str(uuid4()),
        username = username,
        password = password
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user