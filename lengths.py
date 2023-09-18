'''
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise.)
'''


def list_length(list):
    i = 0
    for _ in list:
        i += 1
    return i


def str_length(str):
    i = 0
    for _ in str:
        i += 1
    return i
