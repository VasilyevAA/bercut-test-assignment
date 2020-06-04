import pytest

from calc_app import app


@pytest.fixture(scope='session')
def test_client():
    flask_app = app.run_app()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()


################################
# accessible resources
################################


def __post_formatted_request(client, uri, json_req):
    #  TODO: add logger
    data = client.post(uri, json=json_req)
    return data.status_code, data.json


@pytest.fixture(scope='session')
def additional_request(test_client):
    return lambda req_json: __post_formatted_request(test_client, "/v1/add", req_json)


@pytest.fixture(scope='session')
def difference_request(test_client):
    return lambda req_json: __post_formatted_request(test_client, "/v1/diff", req_json)


@pytest.fixture(scope='session')
def multiplication_request(test_client):
    return lambda req_json: __post_formatted_request(test_client, "/v1/multi", req_json)


@pytest.fixture(scope='session')
def division_request(test_client):
    return lambda req_json: __post_formatted_request(test_client, "/v1/div", req_json)
