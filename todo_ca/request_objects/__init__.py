from ca_util import ValidRequestObject


class EmptyRequestObject(ValidRequestObject):
    @classmethod
    def from_dict(cls, adict):
        return cls()
