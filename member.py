'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x 
and a list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does,but for the sake of the 
exercise you should pretend Python did not have this operator.)
'''


def is_member(x, a):
    if x in a:
        return True
    else:
        return False


def is_member2(x, a):
    status = 0
    for i in a:
        if x == i:
            return True
        status = 1
    if status == 0:
        return False
