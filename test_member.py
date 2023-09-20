from member import is_member, is_member2


def test_member():
    assert is_member('c', ['a', 1, 2, 3, 'c'])


def test_member2():
    assert is_member2('a', ['a', 1, 2, 3, 'b'])
