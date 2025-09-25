from flask.views import MethodView
from flask_smorest import Blueprint
from flaskr.controllers.admin_controller import AdminController
from flaskr.schemas.admin_schema import AdminSchema

blp = Blueprint("admin", "admin", url_prefix="/api/v1/admin")


@blp.route("/create")
class CreateAdmin(MethodView):
    @blp.arguments(AdminSchema)
    def post(self, admin_data):
        return AdminController.create_admin()


@blp.route("/exists")
class CheckAdminExists(MethodView):
    def get(self):
        return AdminController.check_admin_exists()