from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.task_controller import TaskController
from flaskr.schemas.schema import TaskSchema, UpdateTaskSchema

bp = Blueprint("tasks", __name__)


@bp.route("/tasks")
class Tasks(MethodView):
    @jwt_required()
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        """Get all tasks - Protected route (JWT Required)"""
        return TaskController.get_all()

    @jwt_required()
    @bp.arguments(TaskSchema)
    @bp.response(201)
    def post(self, data):
        """Create new task - Protected route (JWT Required)"""
        return TaskController.create(data)


@bp.route("/tasks/user")
class TasksOnUser(MethodView):
    @jwt_required()
    @bp.response(200, TaskSchema(many=True))
    def get(self):
        """Protected route (JWT Required)"""
        return TaskController.get_all_on_user()


@bp.route("/tasks/<task_id>")
class TaskById(MethodView):
    @jwt_required()
    @bp.response(200, TaskSchema)
    def get(self, task_id):
        """Get task by ID - Protected route (JWT Required)"""
        return TaskController.get_by_id(task_id)

    @jwt_required()
    @bp.arguments(UpdateTaskSchema)
    @bp.response(200)
    def put(self, data, task_id):
        """Update entire task - Protected route (JWT Required)"""
        return TaskController.update(data, task_id)

    @jwt_required()
    @bp.arguments(UpdateTaskSchema)
    @bp.response(200)
    def patch(self, data, task_id):
        """Partially update task - Protected route (JWT Required)"""
        return TaskController.patch(data, task_id)

    @jwt_required()
    @bp.response(204)
    def delete(self, task_id):
        """Delete task - Protected route (JWT Required)"""
        return TaskController.delete(task_id)
