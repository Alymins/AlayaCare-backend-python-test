from . import db, app
from test.add_data import start_db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import List


class Users(db.Model):
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    todos: Mapped[List["Todos"]] = relationship(back_populates="user_todos")

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username
        }


class Todos(db.Model):
    __tablename__ = "todos_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    completed: Mapped[str] = mapped_column(String(20), default="unchecked", nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    user_todos: Mapped[List["Users"]] = relationship(back_populates='todos')

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'completed': self.completed,
            'user_id': self.user_id,
        }


def initdb():
    with app.app_context():
        db.create_all()
        start_db()
