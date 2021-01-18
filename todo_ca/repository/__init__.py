import abc


class RepoInterface(abc.ABC):
    @abc.abstractmethod
    def get_todo_list(self):
        pass

    @abc.abstractmethod
    def get_todo(self, todo_id):
        pass

    @abc.abstractmethod
    def create_todo(self, title):
        pass

    @abc.abstractmethod
    def update_todo(self, todo_id: int, title: str, completed: bool):
        pass

    @abc.abstractmethod
    def delete_todo(self, todo_id: int) -> bool:
        pass
