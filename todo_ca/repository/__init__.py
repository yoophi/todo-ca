import abc


class BaseRepo(abc.ABC):
    @abc.abstractmethod
    def get_todo_list(self):
        pass

    @abc.abstractmethod
    def get_todo(self, todo_id):
        pass
