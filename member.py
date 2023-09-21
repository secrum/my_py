'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x 
and a list of values a, and returns True if x is a member of a, False otherwise.
(Note that this is exactly what the in operator does,but for the sake of the 
exercise you should pretend Python did not have this operator.)
'''


def is_member(itm, lst):
    return itm in lst


def is_member2(itm, lst):
    for elem in lst:
        if elem == itm:
            return True
    return False
