from flask import current_app
from werkzeug.local import LocalProxy

from todo_ca.domain.todo import Todo
from todo_ca.repository.mem import MemRepo
from todo_ca.repository.sqla.repo import SqlaRepo
from todo_ca.rest.database import db

todos = [
    Todo.from_dict(
        {
            "id": 1,
            "title": "todo 1",
            "completed": True,
        },
    ),
    Todo.from_dict(
        {
            "id": 2,
            "title": "todo 2",
            "completed": True,
        },
    ),
    Todo.from_dict(
        {
            "id": 3,
            "title": "todo 3",
            "completed": False,
        },
    ),
]

app_repo = None


def get_repo():
    global app_repo, todos

    if app_repo is None:
        if current_app.config.get("REPOSITORY_TYPE") == "sqla":
            app_repo = SqlaRepo(db=db)
        elif current_app.config.get("REPOSITORY_TYPE") == "mem":
            app_repo = MemRepo(todos=todos)
        else:
            app_repo = MemRepo(todos=todos)

    return app_repo


repo = LocalProxy(get_repo)
