""" 
Write a function translate() that will translate a text into "rövarspråket" 
(Swedish for "robber's language"). That is, double every consonant and place
 an occurrence of "o" in between. For example, translate("this is fun") should 
 return the string "tothohisos isos fofunon".
"""

vowels = ["a", "e", "i", "o", "u", " "]


def translate(x):
    char = ""
    for i in x:
        if i in vowels:
            char = char + i
        else:
            char = char + i + "o" + i
    print(char)


translate("this is fun")
