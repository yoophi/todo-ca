from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from todo_ca.repository import RepoInterface
from todo_ca.repository.sqla.models import Todo


class SqlaRepo(RepoInterface):
    def __init__(self, db=None):
        self.db = db

    @property
    def session_context(self):
        if self.db:

            @contextmanager
            def session_scope():
                yield self.db.session

        else:

            @contextmanager
            def session_scope():
                Session = sessionmaker(bind=self.engine)
                session = Session()
                try:
                    yield session
                    session.commit()
                except:
                    session.rollback()
                    raise
                finally:
                    session.close()

        return session_scope

    def get_todo_list(self):
        with self.session_context() as session:
            qry = session.query(Todo)
            todos = qry.all()

        return [item.to_entity() for item in todos]

    def get_todo(self, todo_id):
        with self.session_context() as session:
            todo = session.query(Todo).get(todo_id)

        return todo.to_entity()

    def create_todo(self, title):
        with self.session_context() as session:
            todo = Todo(title=title, completed=False)
            session.add(todo)
            session.commit()

        return todo.to_entity()

    def update_todo(self, todo_id: int, title: str, completed: bool):
        with self.session_context() as session:
            todo = session.query(Todo).get(todo_id)
            if title:
                todo.title = title
            if isinstance(completed, bool):
                todo.completed = completed

            session.add(todo)
            session.commit()

        return todo.to_entity()

    def delete_todo(self, todo_id: int) -> bool:
        with self.session_context() as session:
            todo = session.query(Todo).get(todo_id)
            if todo:
                session.delete(todo)
                session.commit()

        return True
