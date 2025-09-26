import flaskr.models

import os
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from flaskr.extensions import migrate, api, cors, jwt
from flaskr.db import db

from flaskr.routes.auth_route import bp as auth_route
from flaskr.routes.user_route import bp as user_route
from flaskr.routes.tag_route import bp as tag_route
from flaskr.routes.task_route import bp as task_route
from flaskr.routes.user_task_route import blp as user_task_route
from flaskr.routes.admin_route import blp as admin_route


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        if os.getenv('FLASK_ENV') == 'production':
            app.config.from_object(ProductionConfig)
        else:
            app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    api.register_blueprint(auth_route, url_prefix="/api/v1")
    api.register_blueprint(user_route, url_prefix="/api/v1")
    api.register_blueprint(tag_route, url_prefix="/api/v1")
    api.register_blueprint(task_route, url_prefix="/api/v1")
    api.register_blueprint(user_task_route)
    api.register_blueprint(admin_route)

    return app
