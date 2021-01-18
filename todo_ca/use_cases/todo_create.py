from ca_util import UseCase, ResponseSuccess, ResponseFailure

from todo_ca.repository import RepoInterface
from todo_ca.request_objects.todo_create import TodoCreateRequestObject


class TodoCreateUseCase(UseCase):
    def __init__(self, repo: RepoInterface):
        self.repo = repo

    def process_request(self, request_object: TodoCreateRequestObject):
        title = request_object.title
        todo = self.repo.create_todo(title)
        if todo is None:
            return ResponseFailure.build_resource_error(f"todo create failed")

        return ResponseSuccess(value=todo)
