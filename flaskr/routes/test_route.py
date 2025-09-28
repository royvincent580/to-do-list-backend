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
            with db.engine.connect() as conn:
                result = conn.execute(db.text("SELECT name FROM sqlite_master WHERE type='table' AND name='user_tasks';"))
                user_tasks_exists = result.fetchone() is not None
                
                # Get all tables
                result = conn.execute(db.text("SELECT name FROM sqlite_master WHERE type='table';"))
                tables = [row[0] for row in result.fetchall()]
            
            return {
                "user_tasks_table_exists": user_tasks_exists,
                "all_tables": tables
            }
        except Exception as e:
            return {"error": str(e)}, 500

@bp.route("/migrate")
class TestMigrate(MethodView):
    def post(self):
        """Manually trigger database migration"""
        try:
            from flask_migrate import upgrade
            upgrade()
            return {"message": "Migration completed successfully"}
        except Exception as e:
            return {"error": str(e)}, 500