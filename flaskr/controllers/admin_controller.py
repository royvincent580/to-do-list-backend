from flask import request
from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from flaskr.models.admin_model import AdminModel
from flaskr.db import db


class AdminController:
    @staticmethod
    def create_admin():
        try:
            # Check if admin already exists
            existing_admin = db.session.execute(
                select(AdminModel)
            ).scalar_one_or_none()
            
            if existing_admin:
                abort(400, message="Admin already exists. Only one admin is allowed.")
            
            data = request.get_json()
            
            # Create the single admin
            admin = AdminModel(
                email=data["email"],
                password=generate_password_hash(data["password"])
            )
            
            db.session.add(admin)
            db.session.commit()
            
            return {"message": "Admin created successfully"}, 201
            
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while creating admin")
    
    @staticmethod
    def check_admin_exists():
        try:
            existing_admin = db.session.execute(
                select(AdminModel)
            ).scalar_one_or_none()
            
            return {"admin_exists": existing_admin is not None}
            
        except SQLAlchemyError:
            abort(500, message="Internal server error while checking admin")