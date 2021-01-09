from typing import List

from todo_ca.domain.todo import Todo
from todo_ca.repository import BaseRepo


class MemRepo(BaseRepo):
    def __init__(self, todos: List[Todo]):
        self.todos = todos

    def get_todo_list(self):
        return self.todos
