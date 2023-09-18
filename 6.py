'''
Define a function sum() and a function multiply() that sums and multiplies
should return 10, and multiply([1, 2, 3, 4]) should return 24.
'''

li = [1, 2, 3, 4]


def sum(x):
    s = 0
    for i in x:
        s += i
    print(s)


sum(li)


def multiply(x):
    m = 1
    for i in x:
        m *= i
    return m


print(multiply(li))
