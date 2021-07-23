from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from todo_ca.repository.sqla import Base

db = SQLAlchemy(model_class=Base)

import todo_ca.repository.sqla.models  # noqa

migrate = Migrate()
