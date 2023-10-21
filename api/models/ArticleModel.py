from sqlalchemy.dialects.postgresql import JSON
from ..database.db import db
from typing import Dict
from datetime import datetime

class ArticleModel(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.String(36), primary_key=True)
    uid = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String())
    json = db.Column(JSON)
    brief_description = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id: str = None, uid: str = None, title: str = None, json_data: str = None, brief_description: str = None) -> None:
        self.id = id
        self.uid = uid
        self.title = title
        self.json = json_data
        self.brief_description = brief_description

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'uid': self.uid,
            'title': self.title,
            'json_data': self.json,
            'brief_description': self.brief_description,
            'date_created': self.date_created
        }
        
