from flaskr.db import db
from sqlalchemy_serializer import SerializerMixin


class AdminModel(db.Model, SerializerMixin):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    serialize_rules = ('-password',)
    
    def __repr__(self):
        return f"<Admin {self.email}>"