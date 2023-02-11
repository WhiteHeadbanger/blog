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

def create_article(uid: str, title: str, json_data: str, brief_description: str):
    new_article = am.ArticleModel(
        id = str(uuid4()),
        uid = uid,
        title = title,
        json_data = json_data,
        brief_description = brief_description
    )
    
    db.session.add(new_article)
    db.session.commit() 

    return new_article.serialize()

def edit_article(title: str = None, brief_description: str = None, json = None, article_id: str = None):
    article = get_article_by_id(article_id)
    article.title = title
    article.brief_description = brief_description
    article.json = json
    db.session.commit()

    return article.serialize()

def delete_article(article_object: am.ArticleModel):
    article = article_object.serialize()
    db.session.delete(article_object)
    db.session.commit()

    return article

def get_users():
    pass

def get_user_by_username(username: str):
    return um.UserModel.query.filter_by(username = username).first()

def get_user_by_uid(uid: str):
    return um.UserModel.query.filter_by(id = uid).first()

def create_user(username: str, first_name: str, last_name: str, password: str):
    new_user = um.UserModel(
        id = str(uuid4()),
        username = username,
        password = password,
        first_name = first_name,
        last_name = last_name
    )

    db.session.add(new_user)
    db.session.commit()

    return new_user