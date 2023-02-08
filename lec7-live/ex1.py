import os
import math

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Question1: Part A
#
# Using just one line of a Python code, reverse the string "Was it a cat I saw"

s = "Was it a cat I saw"

x = s[::-1]

assert x == "was I tac a ti saW"

# Question 1: Part B
#
# Using methods from Lecture 5, remove spaces and capitalization and write a function
# that returns TRUE if the string is a palindrome and FALSE otherwise.


def palcheck(phrase):
    x = phrase.replace(" ", "").lower()
    s = x[::-1]
    if x == s:
        return True
    else:
        return False


p1 = "Never Odd Or Even"
p2 = "Was It A Rat I Saw"

np1 = "Living after Moosehead"
np2 = "Never odd or event"

assert palcheck(p1) == True
assert palcheck(p2) == True
assert palcheck(np1) == False
assert palcheck(np2) == False
