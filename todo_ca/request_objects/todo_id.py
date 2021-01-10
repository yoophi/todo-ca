from dataclasses import dataclass

from ca_util import ValidRequestObject, InvalidRequestObject


@dataclass
class TodoIdRequestObject(ValidRequestObject):
    todo_id: int

    @classmethod
    def from_dict(cls, adict):
        invalid_request_object = InvalidRequestObject()

        todo_id = adict.get("todo_id")
        if not todo_id:
            return invalid_request_object

        return cls(todo_id=todo_id)
