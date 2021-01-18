from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Todo:
    id: int
    title: str
    completed: bool

    @classmethod
    def from_dict(cls, adict: Optional[Dict] = None, **kwargs):
        if not adict:
            adict = kwargs

        kwargs = {}
        for k in (
            "id",
            "title",
            "completed",
        ):
            kwargs[k] = adict.get(k)

        return cls(**kwargs)

    @property
    def is_completed(self):
        return self.completed is True
