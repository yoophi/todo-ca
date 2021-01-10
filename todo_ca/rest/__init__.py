from flask import Flask

from todo_ca.rest.config import config
from todo_ca.rest.extensions import cors, ma


def create_app(config_name="default", settings_override=None):
    app = Flask(__name__)
    app_config = config[config_name]
    app.config.from_object(app_config)
    app_config.init_app(app)

    init_extensions(app)

    if settings_override:
        app.config.update(settings_override)

    init_blueprint(app)

    return app


def init_blueprint(app: Flask):
    from .api import api as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")


def init_extensions(app):
    cors.init_app(
        app,
        resources={
            r"/*": {"origins": "*"},
        },
    )
    ma.init_app(app)
