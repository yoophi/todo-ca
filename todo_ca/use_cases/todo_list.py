from ca_util import UseCase, ResponseSuccess

from todo_ca.request_objects import EmptyRequestObject


class TodoListUseCase(UseCase):
    def process_request(self, request_object: EmptyRequestObject):
        return ResponseSuccess(value=[])
