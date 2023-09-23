from overlapping import overlapping


def negative_test_overlapping():
    assert overlapping([5, 155555, 8, 6], [1, 2, 3, 4]) is False


def test_overlapping():
    assert overlapping([2, 155555, 8, 6], [1, 2, 3, 4])
