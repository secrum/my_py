'''
The function max() from exercise 1) and the function max_of_three() from exercise 
2) will only work for two and three numbers, respectively. But suppose we have a 
much larger number of numbers, or suppose we cannot tell in advance how many they
are? Write a function max_in_list() that takes a list of numbers and returns the
largest one.
'''


def max_in_list(list):
    max_num = list[0]
    for num in list[1:]:
        if num > max_num:
            max_num = num
    return max_num
