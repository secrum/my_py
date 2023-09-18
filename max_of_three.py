'''
Define a function max_of_three() that takes three numbers as
arguments and returns the largest of them.
'''


def max_of_three(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
