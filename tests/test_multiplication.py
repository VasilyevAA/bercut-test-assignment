import pytest

from tests.utils import STATUS_CODES


@pytest.mark.parametrize('arg1, arg2, expected_result', [
    ('0', '123', '0'),
    ('0', '-0.12', '0'),
    ('-1', '2', '-2'),
    ('-0.2', '0.3', '-0.06'),
    ('-4', '-5.6', '22.4'),
    ('-0.000001', '0.000001', '-1E-12'),
    ('1231231', '2', '2462462'),
    ('20', '2.5', '50.0'),
    ('9'*20, '9'*20+'.01', '9.999999999999999999801000000E+39')
])
@pytest.mark.parametrize('reverse_args', [True, False])
def test_positive_multiplication(multiplication_request, arg1, arg2, expected_result, reverse_args):
    if reverse_args:
        arg1, arg2 = arg2, arg1
    code, data = multiplication_request({'arg1': arg1, 'arg2': arg2})
    assert code == STATUS_CODES.ok
    assert data['result'] == expected_result
