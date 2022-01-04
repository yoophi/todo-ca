from ca_util import ResponseSuccess, ResponseFailure

from todo_ca.domain.todo import Todo
from todo_ca.request_objects.todo_id import TodoIdRequestObject
from todo_ca.use_cases.todo_detail import TodoDetailUseCase
from todo_ca.use_cases.todo_list import TodoListUseCase


def test_todo_list(mocker, client):
    method = mocker.patch.object(
        TodoListUseCase,
        'execute',
        return_value=ResponseSuccess([]),
    )
    res = client.get('/api/todos')
    method.assert_called()

    assert res.status_code == 200


def test_todo_list_fail(mocker, client):
    method = mocker.patch.object(
        TodoListUseCase,
        'execute',
        return_value=ResponseFailure.build_parameters_error()
    )
    res = client.get('/api/todos')
    method.assert_called()

    assert res.status_code == 400


def test_todo_detail(mocker, client):
    method = mocker.patch.object(
        TodoDetailUseCase,
        'execute',
        return_value=ResponseSuccess(Todo.from_dict({
            'id': 1, 'title': 'sample', 'completed': False,
        }))
    )
    res = client.get('/api/todos/1')
    method.assert_called()
    method.assert_called_with(
        TodoIdRequestObject.from_dict({'todo_id': 1}))

    assert res.status_code == 200


def test_todo_detail_fail(mocker, client):
    method = mocker.patch.object(
        TodoDetailUseCase,
        'execute',
        return_value=ResponseFailure.build_resource_error()
    )
    res = client.get('/api/todos/1')
    method.assert_called()

    assert res.status_code == 404
