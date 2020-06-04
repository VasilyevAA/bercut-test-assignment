import pytest

from tests.utils import STATUS_CODES


@pytest.mark.parametrize(
    'arg1, arg2, expected_result',
    [
        ('1', '2', '3'),
        ('-3', '4', '1'),
        ('-6', '5', '-1'),
        ('0.1', '1', '1.1'),
        ('-1.8', '1.1', '-0.7'),
        ('-1.8', '-10', '-11.8'),
        ('1.8', '1.2', '3'),
        ('0', '1.2', '1.2'),
        ('-0.000000', '11', '11'),
        ('9'*27, '9'*27, '1999999999999999999999999998'),
    ]
)
@pytest.mark.parametrize('reverse_args', [True, False])
def test_positive_additional(additional_request, arg1, arg2, expected_result, reverse_args):
    if reverse_args:
        arg1, arg2 = arg2, arg1
    code, data = additional_request({'arg1': arg1, 'arg2': arg2})
    assert code == STATUS_CODES.ok
    assert data['result'] == expected_result
