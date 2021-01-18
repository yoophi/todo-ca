from typing import List

from todo_ca.domain.todo import Todo
from todo_ca.repository import BaseRepo


class MemRepo(BaseRepo):
    def __init__(self, todos: List[Todo]):
        self.todos = todos

    def get_todo_list(self):
        return self.todos

    def get_todo(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo

    def create_todo(self, title):
        todos = self.get_todo_list()
        new_id = max(*[item.id for item in todos]) + 1
        todo = Todo.from_dict(id=new_id, title=title, completed=False)
        self.todos.append(todo)

        return todo

    def update_todo(self, todo_id, title, completed):
        todos = self.get_todo_list()
        new_todos = []
        updated_todo = None
        for todo in todos:
            if todo.id == todo_id:
                if title is not None:
                    todo.title = title
                if isinstance(completed, bool):
                    todo.completed = completed

                updated_todo = todo

            new_todos.append(todo)

        self.todos = new_todos

        return updated_todo

    def delete_todo(self, todo_id: int):
        todos = self.get_todo_list()
        new_todos = []
        todo_deleted = False
        for todo in todos:
            if todo.id == todo_id:
                todo_deleted = True
                continue

            new_todos.append(todo)

        self.todos = new_todos

        return todo_deleted
