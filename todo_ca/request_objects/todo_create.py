from dataclasses import dataclass

from ca_util import ValidRequestObject, InvalidRequestObject


@dataclass
class TodoCreateRequestObject(ValidRequestObject):
    title: str

    @classmethod
    def from_dict(cls, adict):
        invalid_request_object = InvalidRequestObject()

        title = adict.get("title")
        if not title:
            return invalid_request_object

        return cls(title=title)
