from ca_util import UseCase, ResponseSuccess, ResponseFailure

from todo_ca.repository import RepoInterface
from todo_ca.request_objects.todo_update import TodoUpdateRequestObject


class TodoUpdateUseCase(UseCase):
    def __init__(self, repo: RepoInterface):
        self.repo = repo

    def process_request(self, request_object: TodoUpdateRequestObject):
        todo_id = request_object.todo_id
        title = request_object.title
        completed = request_object.completed

        todo = self.repo.update_todo(todo_id=todo_id, title=title, completed=completed)
        if todo is None:
            return ResponseFailure.build_resource_error(f"todo update failed")

        return ResponseSuccess(value=todo)
