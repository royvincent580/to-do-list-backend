from sqlalchemy import String, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flaskr.db import db


class UserTaskModel(db.Model):
    __tablename__ = "user_tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    role = Column(String(50), default="collaborator")  # owner, collaborator, viewer
    joined_at = Column(DateTime, default=func.now())

    # Relationships
    user = relationship("UserModel", back_populates="user_tasks")
    task = relationship("TaskModel", back_populates="user_tasks")