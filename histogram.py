'''
Define a procedure histogram() that takes a list of integers and prints a 
histogram to the screen. For example, histogram([4, 9, 7]) should print the 
following:

****
*********
*******
'''


def histogram(list):
    char = '*'
    res = ""
    for i in list:
        a = i * char + '\n'
        res += a
    return res
