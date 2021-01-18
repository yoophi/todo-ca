from flask import Blueprint, jsonify, request

from todo_ca.rest.repo import repo
from todo_ca.rest.schema import TodoSchema

api = Blueprint("api", __name__)


@api.route(
    "/todos",
    methods=[
        "GET",
    ],
)
def todo_list():
    from todo_ca.use_cases import todo_list as uc
    from todo_ca.request_objects import EmptyRequestObject

    use_case = uc.TodoListUseCase(repo=repo)
    request_object = EmptyRequestObject.from_dict({})
    resp = use_case.execute(request_object)

    if not resp:
        return jsonify(message=resp.message), 400

    schema = TodoSchema(many=True)
    return jsonify(schema.dump(resp.value))


@api.route(
    "/todos/<int:todo_id>",
    methods=[
        "GET",
    ],
)
def todo_detail(todo_id):
    from todo_ca.use_cases import todo_detail as uc
    from todo_ca.request_objects.todo_id import TodoIdRequestObject

    use_case = uc.TodoDetailUseCase(repo=repo)
    request_object = TodoIdRequestObject.from_dict(dict(todo_id=todo_id))
    resp = use_case.execute(request_object)

    if not resp:
        return jsonify(message=resp.message), 404

    schema = TodoSchema()
    return jsonify(schema.dump(resp.value))


@api.route(
    "/todos",
    methods=[
        "POST",
    ],
)
def todo_create():
    from todo_ca.use_cases import todo_create as uc
    from todo_ca.request_objects.todo_create import TodoCreateRequestObject

    payload = request.get_json()
    use_case = uc.TodoCreateUseCase(repo=repo)
    request_object = TodoCreateRequestObject.from_dict(dict(title=payload.get("title")))
    resp = use_case.execute(request_object)

    if not resp:
        return jsonify(message=resp.message), 400

    schema = TodoSchema()
    return jsonify(schema.dump(resp.value))


@api.route(
    "/todos/<int:todo_id>",
    methods=[
        "PUT",
    ],
)
def todo_update(todo_id):
    from todo_ca.use_cases import todo_update as uc
    from todo_ca.request_objects.todo_update import TodoUpdateRequestObject

    payload = request.get_json()
    use_case = uc.TodoUpdateUseCase(repo=repo)
    request_object = TodoUpdateRequestObject.from_dict(
        dict(
            todo_id=todo_id,
            title=payload.get("title"),
            completed=payload.get("completed"),
        )
    )
    resp = use_case.execute(request_object)

    if not resp:
        return jsonify(message=resp.message), 404

    schema = TodoSchema()
    return jsonify(schema.dump(resp.value))
