'''
Define a function max() that takes two numbers as arguments and returns
the largest of them. Use the if-then-else construct available in Python.
(It is true that Python has the max() function built in, but writing it
yourself is nevertheless a good exercise.)
'''


def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(max(222, 443))
