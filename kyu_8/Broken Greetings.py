'''
https://www.codewars.com/kata/50654ddff44f800200000001
Description:

Correct this code, so that the greet function returns the expected value.
'''
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, other_name):
        self.other_name = other_name
        return "Hi {0}, my name is {1}".format(other_name, self.name)