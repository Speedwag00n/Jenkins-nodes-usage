from passlib.apps import custom_app_context as pwd_context

from app import database


class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.BigInteger, primary_key=True, autoincrement=True)
    username = database.Column(database.String(255), nullable=False)
    password = database.Column(database.String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
