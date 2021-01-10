import json

from marshmallow import fields
from .extensions import ma



class TodoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "title",
            "is_completed",
        )

