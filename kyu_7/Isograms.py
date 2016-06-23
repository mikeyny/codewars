'''
https://www.codewars.com/kata/54ba84be607a92aa900000f1
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''
def is_isogram(string):
    import re
    for x in string:
        if len(re.findall(x.lower(),string.lower()))>1:
            return False
    return True