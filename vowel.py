"""
Write a function that takes a character (i.e. a string of length 1) and returns True if 
it is a vowel, False otherwise.
"""

vowels = ["a", "e", "i", "o", "u"]


def is_vowel(char):
    if char in vowels:
        return True
    else:
        return False
