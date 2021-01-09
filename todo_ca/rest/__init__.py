from flask import Flask


def create_app(config):
    app = Flask(__name__)
    init_blueprint(app)

    return app


def init_blueprint(app: Flask):
    from .api import api as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")
