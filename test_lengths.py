from lengths import str_length
from lengths import list_length


def test_str_length():
    assert str_length("Hello world") == 11


def test_list_length():
    lst = ['Vikea', 'Gleb Palkin', 'Mihai Chele',
           'Temciuc', 'Voronin', 'Plaha', 'Chirtoaca']
    assert list_length(lst) == 7
