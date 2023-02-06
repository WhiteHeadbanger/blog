from sqlalchemy.dialects.postgresql import JSON
from database.db import db
from typing import Dict, Any

class ArticleModel(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.String(36), primary_key=True)
    uid = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String())
    html = db.Column(db.String())

    def __init__(self, id: str = None, uid: str = None, title: str = None, html_data: str = None) -> None:
        self.id = id
        self.uid = uid
        self.title = title
        self.html = html_data

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'uid': self.uid,
            'title': self.title,
            'html': self.html
        }
        
