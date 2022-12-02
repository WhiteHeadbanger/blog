from flask_login import UserMixin
from database.db import db
from typing import Dict

class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36), primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(100))

    def __init__(self, id: str = None, username: str = None, password: str = None) -> None:
        self.id = id
        self.username = username
        self.password = password

    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

    @classmethod
    def get_users():
        pass

    @classmethod
    def get_user():
        pass
    

   