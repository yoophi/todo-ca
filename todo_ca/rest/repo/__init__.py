from flask import g
from werkzeug.local import LocalProxy

from todo_ca.domain.todo import Todo
from todo_ca.repository.mem import MemRepo


def get_repo():
    if "repo" not in g:
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

        g.repo = MemRepo(todos=todos)

    return g.repo


repo = LocalProxy(get_repo)
