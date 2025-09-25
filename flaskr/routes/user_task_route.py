from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required
from flaskr.controllers.user_task_controller import UserTaskController
from flaskr.schemas.schema import UserTaskSchema

blp = Blueprint("user_tasks", __name__, description="User task collaboration", url_prefix="/api/v1/tasks")


@blp.route("/collaborative")
class UserCollaborativeTasks(MethodView):
    @jwt_required()
    @blp.response(200)
    def get(self):
        return UserTaskController.get_user_collaborative_tasks()


@blp.route("/<int:task_id>/collaborators")
class TaskCollaborators(MethodView):
    @jwt_required()
    @blp.response(200)
    def get(self, task_id):
        return UserTaskController.get_task_collaborators(task_id)

    @jwt_required()
    @blp.arguments(UserTaskSchema)
    def post(self, collaboration_data, task_id):
        UserTaskController.add_collaborator(task_id, collaboration_data)
        return {"message": "Collaborator added successfully"}, 201