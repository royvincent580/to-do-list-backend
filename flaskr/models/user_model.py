from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, Integer
from flaskr.db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True, index=True)
    email = Column(String(120), nullable=False, unique=True, index=True)
    password = Column(String(300), nullable=False)

    tasks = relationship(
        "TaskModel", back_populates="user", cascade="all, delete-orphan"
    )
    
    # Many-to-many relationship with tasks through collaboration
    user_tasks = relationship("UserTaskModel", back_populates="user", cascade="all, delete-orphan")
