'''
Define a function overlapping() that takes two lists and returns True if they 
have at least one member in common, False otherwise. You may use your is_member()
function, or the in operator, but for the sake of the exercise, you should (also)
write it using two nested for-loops.
'''

from member import is_member

def overlapping(lst1, lst2):
    for itm in lst1:
        if is_member(itm, lst2):
            return True
    return False
        

    #     for itm2 in lst2:
    #         if itm1 == itm2:
    #             return True
    # return False

# def is_member2(itm, lst)jjjjjj
#     for elem in lst:
#         if elem == itm:
#             return True
#     return False
