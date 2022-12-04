from . import PostModel as pm
from . import UserModel as um
from uuid import uuid4
from database.db import db

def get_posts():
    return pm.PostModel.query.all()

def get_post_by_id():
    pass

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

def get_users():
    pass

def get_user():
    pass