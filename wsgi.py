import os

from todo_ca.entrypoints.flask_app import create_app

config = os.environ.get("FLASK_CONFIG", "default")
app = create_app(config)
