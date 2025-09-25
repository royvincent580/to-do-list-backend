from flask.views import MethodView
from flask_smorest import Blueprint
from flaskr.controllers.tag_controller import TagController
from flaskr.schemas.schema import TagSchema

bp = Blueprint("tags", __name__)


@bp.route("/tags")
class Tags(MethodView):
    @bp.response(200, TagSchema(many=True))
    def get(self):
        return TagController.get_all()

    @bp.arguments(TagSchema)
    @bp.response(201)
    def post(self, data):
        return TagController.create(data)


@bp.route("/tags/<tag_id>")
class TagById(MethodView):
    @bp.arguments(TagSchema)
    @bp.response(200, TagSchema)
    def put(self, data, tag_id):
        return TagController.update(data, tag_id)
    
    @bp.response(204)
    def delete(self, tag_id):
        return TagController.delete(tag_id)
