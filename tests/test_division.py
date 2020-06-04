
from tests.utils import STATUS_CODES


def t1est_positive_division_by_number_with_max_count_of_decimals(division_request):
    code, data = division_request({'arg1': '1', 'arg2': '2'})
    assert code == STATUS_CODES.ok
    assert data['result'] == "0.5"


def t1est_positive_division_by_number_with_max_count_of_decimals(division_request):
    code, data = division_request({'arg1': '1', 'arg2': '0.000003'})
    assert code == STATUS_CODES.ok
    assert data['result'] == "333333.3333333333333333333333"


def test_negative_division_by_zero(division_request):
    code, data = division_request({'arg1': '1', 'arg2': '0'})
    assert code == STATUS_CODES.bad
    assert not data


