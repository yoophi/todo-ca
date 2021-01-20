import os

from todo_ca.rest import create_app

config = os.environ.get("FLASK_CONFIG", "default")
app = create_app(config)
