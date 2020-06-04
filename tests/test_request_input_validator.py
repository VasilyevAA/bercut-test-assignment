import pytest

from tests.utils import STATUS_CODES


#  TODO: think about parametrize by each resource. Now we choose white box testing
#   and i think we can aggregate into one equivalence class all enabled resources,
#   because we know what all resources use same validation.
#   And check specific behavior in certain test functional package.


@pytest.mark.parametrize(
    'arg1, arg2, expected_result',
    [
        ('1234567890', '-1', '1234567889'),
        ('0.012345', '-0.678900', '-0.666555'),
        ('-0', '1', '1')
    ],
)
@pytest.mark.parametrize('reverse_args', [True, False])
def test_positive_check_all_numbers_can_be_used(additional_request, arg1, arg2, expected_result, reverse_args):
    if reverse_args:
        arg1, arg2 = arg2, arg1
    code, data = additional_request({"arg1": arg1, "arg2": arg2})
    assert code == STATUS_CODES.ok
    assert data['result'] == expected_result


@pytest.mark.parametrize(
    'invalid_arg',
    ['--1', '+1', '0.0000011', None, 'asdqwe', '0x1', '', 'undefined'],
)
@pytest.mark.parametrize('invalid_first_arg', [True, False])
def test_negative_request_validator_with_invalid_values(additional_request, invalid_arg, invalid_first_arg):
    if invalid_first_arg:
        arg1, arg2 = invalid_arg, '1'
    else:
        arg1, arg2 = '1', invalid_arg
    code, data = additional_request({"arg1": arg1, "arg2": arg2})
    assert code == STATUS_CODES.bad
    assert data['error']


@pytest.mark.parametrize('req_json', [{'arg1': '1'}, {'arg2': '1'}])
def test_negative_request_validator_without_some_arg(additional_request, req_json):
    code, data = additional_request(req_json)
    assert code == STATUS_CODES.bad
    assert data['error']
