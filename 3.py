'''
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in,
but writing it yourself is nevertheless a good exercise.)
'''
# list
my_list = ['Vikea', 'Gleb Palkin', 'Mihai Chele',
           'Temciuc', 'Voronin', 'Plaha', 'Chirtoaca']


def list_length():
    i = 0
    for x in my_list:
        i = i + 1
    print(i)


list_length()

# string
my_str = 'Viiiikkeaaaaaaaaaaaaaaaaa!!!'


def str_length(x):
    i = 0
    for x in my_str:
        i = i + 1
    return i


print(str_length(my_str))
