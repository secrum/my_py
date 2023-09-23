from histogram import histogram


def test_histogram():
    assert histogram([3, 4, 5, 6, 7, 8]) == '''***
****
*****
******
*******
********
'''
