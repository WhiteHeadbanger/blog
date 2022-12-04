from . import PostModel as pm
from . import UserModel as um
from uuid import uuid4
from database.db import db

def get_posts():
    return pm.PostModel.query.all()

def get_post_by_id(id: str):
    return pm.PostModel.query.filter_by(id = id).one()

def get_post_by_uid(uid: str):
    return pm.PostModel.query.filter_by(uid = uid).all()

def create_post(uid: str, title: str, body: str):
    new_post = pm.PostModel(
        id = str(uuid4()),
        uid = uid,
        title = title,
        body = body
    )
    
    db.session.add(new_post)
    db.session.commit() 

    return new_post.serialize()

def edit_post(post_obj: pm.PostModel, title: str = None, body: str = None):
    post_obj.title = title
    post_obj.body = body
    db.session.commit()

    return post_obj.serialize()

def delete_post(post_obj: pm.PostModel):
    post = post_obj.serialize()
    db.session.delete(post_obj)
    db.session.commit()

    return post

def get_users():
    pass

def get_user():
    pass