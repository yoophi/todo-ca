from ca_util import UseCase, ResponseSuccess, ResponseFailure

from todo_ca.repository import BaseRepo
from todo_ca.request_objects.todo_id import TodoIdRequestObject


class TodoDetailUseCase(UseCase):
    def __init__(self, repo: BaseRepo):
        self.repo = repo

    def process_request(self, request_object: TodoIdRequestObject):
        todo_id = request_object.todo_id
        todo = self.repo.get_todo(todo_id)
        if todo is None:
            return ResponseFailure.build_resource_error(
                f"todo with id:{todo_id} not found"
            )

        return ResponseSuccess(value=todo)
