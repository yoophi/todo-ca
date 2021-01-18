from todo_ca.domain.todo import Todo
from todo_ca.repository.mem import MemRepo

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

repo = MemRepo(todos=todos)
