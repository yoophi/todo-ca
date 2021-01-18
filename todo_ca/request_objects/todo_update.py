from dataclasses import dataclass
from typing import Optional

from ca_util import ValidRequestObject, InvalidRequestObject


@dataclass
class TodoUpdateRequestObject(ValidRequestObject):
    todo_id: int
    title: Optional[str]
    completed: Optional[bool]

    @classmethod
    def from_dict(cls, adict):
        invalid_request_object = InvalidRequestObject()

        todo_id = adict.get("todo_id")
        title = adict.get("title")
        completed = adict.get("completed")

        if not todo_id or (not title and completed is None):
            return invalid_request_object

        return cls(todo_id=todo_id, title=title, completed=completed)
