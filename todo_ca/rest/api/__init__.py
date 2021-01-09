from dataclasses import asdict

from flask import Blueprint, jsonify, current_app

from todo_ca.rest.repo import repo

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

    return jsonify([asdict(item) for item in resp.value])
