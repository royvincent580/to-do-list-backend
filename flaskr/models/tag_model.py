from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from flaskr.db import db


class TagModel(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, index=True, unique=True)

    # Many-to-many relationship with tasks through association table
    task_tags = relationship("TaskTagModel", back_populates="tag", cascade="all, delete-orphan")
