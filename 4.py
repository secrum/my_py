"""
Write a function that takes a character (i.e. a string of length 1) and returns True if 
it is a vowel, False otherwise.
"""

vowels = ["a", "e", "i", "o", "u"]


def is_wowel(x):
    if x in vowels:
        return True
    else:
        return False


print(is_wowel("u"))
