from flask.views import MethodView
from flask_smorest import Blueprint
from flaskr.db import db

bp = Blueprint("test", __name__, url_prefix="/api/v1/test")

@bp.route("/tables")
class TestTables(MethodView):
    def get(self):
        """Test endpoint to check if tables exist"""
        try:
            # Check if user_tasks table exists
            result = db.engine.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user_tasks';")
            user_tasks_exists = result.fetchone() is not None
            
            # Get all tables
            result = db.engine.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in result.fetchall()]
            
            return {
                "user_tasks_table_exists": user_tasks_exists,
                "all_tables": tables
            }
        except Exception as e:
            return {"error": str(e)}, 500