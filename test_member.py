from member import is_member, is_member2


def test_member():
    assert is_member('c', ['a', 1, 2, 3, 'c'])


def test_member_is_not_member():
    assert is_member('b', ['a', 1, 2, 3, 'c']) is False


def test_member2():
    assert is_member2('b', ['a', 1, 2, 3, 'b'])


def test_member2_is_not_member():
    assert is_member2('x', ['a', 1, 2, 3, 'b']) is False
