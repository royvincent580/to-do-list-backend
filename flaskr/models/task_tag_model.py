from sqlalchemy import ForeignKey, String, DateTime, Column, Integer
from sqlalchemy.orm import relationship
from flaskr.db import db
from datetime import datetime, timezone


class TaskTagModel(db.Model):
    __tablename__ = "task_tags"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
    
    # User submittable attribute (required by Phase 4)
    priority = Column(String(10), nullable=False, default="medium")
    assigned_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    task = relationship("TaskModel", back_populates="task_tags")
    tag = relationship("TagModel", back_populates="task_tags")