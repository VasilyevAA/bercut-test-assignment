import pytest

from tests.utils import STATUS_CODES


@pytest.mark.parametrize('arg1, arg2')
@pytest.mark.parametrize('reverse_args', [True, False])
def test_positive_multiplication(multiplication_request, arg1, arg2, reverse_args):
    if reverse_args:
        arg1, arg2 = arg2, arg1
    code, data = multiplication_request({'arg1': arg1, 'arg2': arg2})
    assert code == STATUS_CODES.ok