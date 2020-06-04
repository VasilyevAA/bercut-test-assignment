import pytest

from tests.utils import STATUS_CODES


@pytest.mark.parametrize(
    'arg1, arg2, expected_result',
    [
        ('2', '2', '1'),
        ('3', '-3', '-1'),
        ('4', '0.1', '40'),
        ('5', '1.25', '4'),
        ('15', '-2.500000', '-6'),

        ('0.1', '4', '0.025'),
        ('10.4', '2.0', '5.2'),
        ('-0.1', '10', '-0.01'),
        ('-1.6', '4', '-0.4'),
        ('-5', '2', '-2.5'),
        ('100', '3', '33.33333333333333333333333333'),

        ('0.000001', '-0.000001', '-1'),
        ('0.000001', '9'*20, '10.0000000000000000001E-27'),
        ('0', '2.0', '0'),
        ('-0', '20', '0'),
        ('0', '-0.222', '0'),
    ]
)
def test_positive_division(division_request, arg1, arg2, expected_result):
    code, data = division_request({'arg1': arg1, 'arg2': arg2})
    assert code == STATUS_CODES.ok
    assert data['result'] == expected_result


def test_negative_division_by_zero(division_request):
    code, data = division_request({'arg1': '1', 'arg2': '0'})
    assert code == STATUS_CODES.bad
    assert data['error']


