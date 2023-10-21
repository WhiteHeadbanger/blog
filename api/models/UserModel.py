from flask_login import UserMixin
from ..database.db import db
from typing import Dict

class UserModel(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36), primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, id: str = None, username: str = None, password: str = None, first_name: str = None, last_name: str = None) -> None:
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name,
        self.last_name = last_name

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
    

   