from flask_jwt_extended import get_jwt_identity
from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from flaskr.db import db
from flaskr.models.user_task_model import UserTaskModel
from flaskr.models.task_model import TaskModel
from flaskr.models.user_model import UserModel


class UserTaskController:
    @staticmethod
    def add_collaborator(task_id, data):
        try:
            current_user_id = get_jwt_identity()
            
            # Check if task exists and user is owner
            task = db.session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            ).scalar_one()
            
            if task.user_id != current_user_id:
                abort(403, message="Only task owner can add collaborators")
            
            # Check if user exists
            try:
                user = db.session.execute(
                    select(UserModel).where(UserModel.email == data["email"])
                ).scalar_one()
            except NoResultFound:
                abort(404, message="User with this email is not registered. Only registered users can be added as collaborators.")
            
            # Check if already collaborating
            existing = db.session.execute(
                select(UserTaskModel).where(
                    UserTaskModel.user_id == user.id,
                    UserTaskModel.task_id == task_id
                )
            ).scalar_one_or_none()
            
            if existing:
                abort(409, message="User already collaborating on this task")
            
            # Add collaboration
            collaboration = UserTaskModel(
                user_id=user.id,
                task_id=task_id,
                role=data.get("role", "collaborator")
            )
            
            db.session.add(collaboration)
            db.session.commit()
            
        except NoResultFound:
            abort(404, message="Task or user not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while adding collaborator")

    @staticmethod
    def get_task_collaborators(task_id):
        try:
            collaborators = db.session.execute(
                select(UserTaskModel, UserModel.username, UserModel.email)
                .join(UserModel, UserTaskModel.user_id == UserModel.id)
                .where(UserTaskModel.task_id == task_id)
            ).all()
            
            return [
                {
                    "id": collab.UserTaskModel.id,
                    "username": collab.username,
                    "email": collab.email,
                    "role": collab.UserTaskModel.role,
                    "joined_at": collab.UserTaskModel.joined_at
                }
                for collab in collaborators
            ]
            
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching collaborators")

    @staticmethod
    def get_user_collaborative_tasks():
        try:
            current_user_id = get_jwt_identity()
            
            # Get all tasks where current user is a collaborator
            collaborative_tasks = db.session.execute(
                select(TaskModel, UserTaskModel.role, UserTaskModel.joined_at)
                .join(UserTaskModel, TaskModel.id == UserTaskModel.task_id)
                .where(UserTaskModel.user_id == current_user_id)
            ).all()
            
            return [
                {
                    "id": task.TaskModel.id,
                    "title": task.TaskModel.title,
                    "description": task.TaskModel.description,
                    "status": task.TaskModel.status,
                    "priority": task.TaskModel.priority,
                    "role": task.role,
                    "joined_at": task.joined_at,
                    "owner_id": task.TaskModel.user_id
                }
                for task in collaborative_tasks
            ]
            
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching collaborative tasks")