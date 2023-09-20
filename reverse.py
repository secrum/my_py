'''
Define a function reverse() that computes the reversal of a string. 
For example, reverse("I am testing")
should return the string "gnitset ma I".
'''


def reverse(str):
    new = []
    for i in range(len(str))[::-1]:
        new.append(str[i])
    return (''.join(new))
