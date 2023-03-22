from todo_api import db, app
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.String(), default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    tasks = db.relationship('Tasks', backref='user', lazy=True)


    def __init__(self, username, password_hash) -> None:
        self.username = username
        self.password_hash = password_hash


    def __repr__(self) -> str:
        return self.username


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(), default='-empty-')
    is_complete = db.Column(db.Boolean(), default=False, nullable=False)
    by_user = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)


    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description
    
    
    def __repr__(self) -> str:
        return self.title
    
