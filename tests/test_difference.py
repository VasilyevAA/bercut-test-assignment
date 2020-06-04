import pytest

from tests.utils import STATUS_CODES


@pytest.mark.parametrize(
    'arg1, arg2, expected_result',
    [
        ('1', '2', '-1'),
        ('-3', '4', '-7'),
        ('-6', '5', '-11'),
        ('0.1', '1', '-0.9'),
        ('-1.8', '1.1', '-2.9'),
        ('-1.8', '-10', '8.2'),
        ('1.8', '1.2', '0.6'),
        ('0', '1.2', '-1.2'),
        ('-0.000000', '11', '-11'),
        ('9'*27, '9'*27, '0'),

        ('2', '1', '1'),
        ('4', '-3', '7'),
        ('1', '0.1', '0.9'),
        ('1.1', '-1.8', '2.9'),
        ('-10', '-1.8', '-8.2'),
        ('1.2', '0', '1.2'),
        ('11', '-0.000000', '11'),
    ]
)
def test_positive_difference(difference_request, arg1, arg2, expected_result):
    code, data = difference_request({'arg1': arg1, 'arg2': arg2})
    assert code == STATUS_CODES.ok
    assert data['result'] == expected_result
