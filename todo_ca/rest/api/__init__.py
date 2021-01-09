from flask import Blueprint, jsonify


api = Blueprint('api', __name__)


@api.route('/todos', methods=['GET', ])
def todo_list():
    from todo_ca.use_cases import todo_list as uc
    from todo_ca.request_objects import EmptyRequestObject

    use_case = uc.TodoListUseCase()
    request_object = EmptyRequestObject.from_dict({})
    resp = use_case.execute(request_object)

    if not resp:
        return jsonify(message='error'), 400

    return jsonify(resp.value)
