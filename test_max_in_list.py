from max_in_list import max_in_list


def test_max_in_list_negative():
    try: 
        max_in_list([])
        assert False
    except Exception as error:
        assert str(error) == "Provided list cannot be empty"


def test_max_in_list():
    assert max_in_list([2, 3, 44, 1, 5, 432, 222, 2, 342, 21, 11]) == 432 
