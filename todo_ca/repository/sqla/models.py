from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    Boolean,
)

from todo_ca.domain.todo import Todo as TodoEntity
from todo_ca.repository.sqla import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column("id", Integer, primary_key=True)
    title = Column(
        "title",
        Unicode,
        nullable=False,
    )
    completed = Column(
        "completed",
        Boolean,
        nullable=False,
        default=False,
    )

    def to_entity(self):
        return TodoEntity.from_dict(
            {
                "id": self.id,
                "title": self.title,
                "completed": self.completed,
            }
        )
