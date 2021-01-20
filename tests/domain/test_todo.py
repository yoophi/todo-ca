from todo_ca.domain.todo import Todo


def test_create_todo_with_adict():
    adict = {
        "id": 1,
        "title": "some title",
        "completed": False,
    }
    todo = Todo.from_dict(adict)

    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert todo.title == "some title"
    assert todo.completed is False
    assert todo.is_completed is False


def test_create_todo_with_kwargs():
    todo = Todo.from_dict(id=1, title="some title", completed=False)

    assert isinstance(todo, Todo)
    assert todo.id == 1
    assert todo.title == "some title"
    assert todo.completed is False
    assert todo.is_completed is False
