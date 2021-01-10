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
