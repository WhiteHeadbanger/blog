from flask_login import UserMixin
from database.db import db
from typing import Dict

class PostModel(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.String(36), primary_key=True)
    uid = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String())
    body = db.Column(db.String())

    def __init__(self, id: str = None, uid: str = None, title: str = None, body: str = None) -> None:
        self.id = id
        self.uid = uid
        self.title = title
        self.body = body

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'uid': self.uid,
            'title': self.title,
            'body': self.body
        }
        
