from ca_util import UseCase, ResponseSuccess, ResponseFailure

from todo_ca.repository import BaseRepo
from todo_ca.request_objects.todo_id import TodoIdRequestObject


class TodoDeleteUseCase(UseCase):
    def __init__(self, repo: BaseRepo):
        self.repo = repo

    def process_request(self, request_object: TodoIdRequestObject):
        todo_id = request_object.todo_id

        res = self.repo.delete_todo(todo_id=todo_id)
        if res is not True:
            return ResponseFailure.build_resource_error(f"todo:{todo_id} delete failed")

        return ResponseSuccess(value=res)
