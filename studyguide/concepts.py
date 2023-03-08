# 1. int, float, bool, None

# 2. Overloaded "+"
# -------------------------------------------------------------------------
class Widget(object):
    def __init__(self):
        self.value = 0

    def getValue(self):
        return self.value

    def setValue(self, x):
        self.value = x

    def __add__(self, other):
        self.value += other.getValue()


w1 = Widget()
w1.setValue(5)

w2 = Widget()
w2.setValue(10)

print("w1: ", w1.getValue())
print("w2: ", w2.getValue())

w1 + w2
print("w1: ", w1.getValue())
print("w2: ", w2.getValue())

w2 + w1
print("w1: ", w1.getValue())
print("w2: ", w2.getValue())

# 3. Iteration and recursion
# -------------------------------------------------------------------------
#
# The recursive "base case" is the one (or multiple!) situations
# where we define the function's value without making reference to itself.
#


def factorial_loop(n):
    total = 1
    j = 1
    while j <= n:
        total = total*j
        j = j+1
    return total


def factorial(n):
    """Assumes input is an int >=0.
    Returns n!"""
    if type(n) == int and n >= 0:
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    else:
        return 'Please enter a non-negative integer.'

# -------------------------------------------------------------------------
# 4. Bisection search works on an ordered list. If the element we are searching for
#    is smaller than the middle of the list we are searching, we look at the lower
#    half of the list, etc. Linear search traverses the whole list.
#
#    Linear search: O(n)
#    Bisection: O(ln(n))
#
#    logy(x) is the number of times y has to be multiplied by itself to reach x.
#    ln(n) is the number of times n has to be split in half before it reaches 0.
#
# -------------------------------------------------------------------------
# 5. formal vs. actual params; local vs. global vars, default values
# -------------------------------------------------------------------------
# x and y are "formal" parameters


def sum(x, y):
    return x + y


# m and n are "actual" parameters
m = 5
n = 6
ans = sum(m, n)  # sum() is executed here for the first time

# global variable
value = 10


def diffGlobal():
    value = 12  # local variable, scoped to diffGlobal()
    return "value = {}".format(value)


print()
print("global value =", value)
print("local ", diffGlobal())

# default params


def someFunc(x, y=-1):
    """Simply prints x and y; y has a default value"""
    return "\nx: {}\ny: {}".format(x, y)


# retrive the docstring
help(someFunc)
print("someFunc(5): ", someFunc(5))
print("someFunc(9, 10): ", someFunc(9, 10))

# 6. Subset-Sum problem
# -------------------------------------------------------------------------
# See Lecture 5
#
#
# 7. Slice notation
# -------------------------------------------------------------------------
x = list(range(0, 20))

print(x)      # whole list
print(x[:5])  # first 5 entries
print(x[5:])  # last 15 entries
print(x[:-1])  # all except last entry
print(x[-1:])  # last entry

# 8.
# -------------------------------------------------------------------------
#   list: unordered collection of anything
#   set: unordered collection of unique elements, has usual
#        "set" operations (union, issubset, ...)
#   tuple: immutable, ordered sequences of elements of any type

# 9. edit distance between strings

#

# Edit distance is the difference in two strings, in character order. If

# one string is empty, the edit differences is the length of the other string.

# -------------------------------------------------------------------------


def edit_distance(s, t):
    """Given two strings s and t it returns the edit distance between them"""
    if len(s) == 0 or len(t) == 0:
        return max(len(s), len(t))
    if s[0] == t[0]:
        return edit_distance(s[1:], t[1:])
    else:
        substitution = 1 + edit_distance(s[1:], t[1:])
        deletion = 1 + edit_distance(s[1:], t)
        insertion = 1 + edit_distance(s, t[1:])
        return min(substitution, deletion, insertion)
        # return substitution


print("edit_distance('aloud','loud'): ", edit_distance('aloud', 'loud'))
print("edit_distance('loud','louder'): ", edit_distance('loud', 'louder'))
print("edit_distance('alien','sales'): ", edit_distance('alien', 'sales'))
