from list_calc import multiply
from list_calc import sum


def test_list_multiply():
    assert multiply([1, 2, 3, 4]) == 24


def test_list_multiply_with_zero():
    assert multiply([1, 2, 0, 4]) == 0


def test_list_sum():
    assert sum([1, 2, 3, 4]) == 10


def test_list_sum_with_zero():
    assert sum([1, 0, 0, 0]) == 1
