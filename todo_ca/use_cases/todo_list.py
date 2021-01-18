from ca_util import UseCase, ResponseSuccess

from todo_ca.repository import RepoInterface
from todo_ca.request_objects import EmptyRequestObject


class TodoListUseCase(UseCase):
    def __init__(self, repo: RepoInterface):
        self.repo = repo

    def process_request(self, request_object: EmptyRequestObject):
        todo_list = self.repo.get_todo_list()

        return ResponseSuccess(value=todo_list)
