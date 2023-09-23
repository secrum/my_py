from nchars import generate_n_chars


def test_nchars():
    assert generate_n_chars(13, 'T') == 'TTTTTTTTTTTTT'
