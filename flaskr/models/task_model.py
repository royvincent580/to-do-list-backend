from enum import Enum
from sqlalchemy import ForeignKey, String, Enum as SaEnum, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from flaskr.db import db
from datetime import datetime, timezone


class TaskStatus(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False, index=True)
    content = Column(String(600), nullable=False)
    status = Column(SaEnum(TaskStatus), nullable=False, default=TaskStatus.PENDING)
    created_at = Column(DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("UserModel", back_populates="tasks")
    
    # Temporary: Keep tag_id for backward compatibility
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=True)
    tag = relationship("TagModel")

    # Many-to-many relationship with tags through association table
    task_tags = relationship("TaskTagModel", back_populates="task", cascade="all, delete-orphan")
    
    # Many-to-many relationship with users through collaboration
    user_tasks = relationship("UserTaskModel", back_populates="task", cascade="all, delete-orphan")
