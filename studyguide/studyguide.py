from functools import cache
import random
import string
import os
import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# ---------------------------------------------------------------------
# Q1
# ---------------------------------------------------------------------


def list_reverse(s):
    try:
        reversed = [0] * len(s)
        for i in range(len(s)):
            reversed[len(s) - 1 - i] = s[i]
        return reversed
    except TypeError as msg:
        print("arg must be a list: ", msg)
        return None


datum = [i for i in range(20)]
assert list_reverse(datum) == [19, 18, 17, 16, 15, 14, 13,
                               12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert list_reverse("cat") == ['t', 'a', 'c']
assert list_reverse(5) == None


# ---------------------------------------------------------------------
# Q2
# ---------------------------------------------------------------------
def int_sum(x, y):
    try:
        if x % 2 == 0 and y % 2 == 0:
            return x * y
        else:
            return x + y
    except TypeError as msg:
        print("args must be integers: ", msg)
        return None


assert int_sum(4, 6) == 24
assert int_sum(4, 5) == 9
assert int_sum(5, 7) == 12
assert int_sum(5, 6) == 11
assert int_sum("ham", "cheese") == None

# ---------------------------------------------------------------------
# Q3
# ---------------------------------------------------------------------


def int_finder(L, m):
    try:
        df = pd.DataFrame(L)
        return df.value_counts()[m]
    except ValueError as msg:
        print("args must be a list of integers, followed by a single integer")
        return None


assert int_finder([1, 23, 4, 2, 56, 7, 6, 2, 2, 2], 2) == 4
assert int_finder("cat", 2) == None


def int_finder2(L, m):
    try:
        count = L.count(m)
        return count
    except TypeError as msg:
        print("args must be a list of integers, followed by a single integer")
        return None


assert int_finder2([1, 23, 4, 2, 56, 7, 6, 2, 2, 2], 2) == 4
assert int_finder2("cat", 2) == None

# ---------------------------------------------------------------------
# Q4
# ---------------------------------------------------------------------


def uniq(L):
    newList = np.unique(L).tolist()
    return newList


assert uniq([1, 2, 32, 14, 2, 1]) == [1, 2, 14, 32]

# ---------------------------------------------------------------------
# Q5
# ---------------------------------------------------------------------


def pick_random(l):
    try:
        return l[random.randrange(len(l))]
    except TypeError as msg:
        print("arg must be a list of any type")
        return None


alphabet = list(string.ascii_lowercase)
print("alphabet: ", alphabet)
ans = pick_random(alphabet)
print("ans: ", ans)

assert pick_random(1) == None

# ---------------------------------------------------------------------
# Q6
# ---------------------------------------------------------------------


def find_smallest(l):
    try:
        smallest = l[0]
        for i in range(len(l)):
            if l[i] < smallest:
                smallest = l[i]
        return smallest
    except TypeError as msg:
        print("arg must be a list: ", msg)
        return None


assert find_smallest([2, 3, 4, 5, 1]) == 1
assert find_smallest(2) == None


def find_smallest2(l):
    try:
        l.sort()
        return l[0]
    except AttributeError as msg:
        print("arg must be a list: ", msg)


assert find_smallest2([2, 3, 4, 5, 1]) == 1
assert find_smallest2(2) == None
assert find_smallest2("cat") == None

# ---------------------------------------------------------------------
# Q7
# ---------------------------------------------------------------------


def vowel_replacer(s):
    try:
        # split incoming string
        data = [*s]
        TARGETS = ['a', 'e', 'i', 'o', 'u']

        for index in range(len(data)):
            if data[index] in TARGETS:
                data[index] = 'y'
        return "".join(str(x) for x in data)
    except TypeError as msg:
        print("arg must be a string value: ", msg)
        return None


assert vowel_replacer(5) == None
assert vowel_replacer("streets") == "stryyts"
assert vowel_replacer("aeiou") == "yyyyy"

# ---------------------------------------------------------------------
# Q8
# ---------------------------------------------------------------------

# cache all calls - cached values are returned instead
# of recalculated


@cache
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_list(m):

    # Work in reverse order, only the first call invokes the recursive
    # call, the rest just return the cached value.
    current = m
    fibList = []
    while current > -1:
        fibList.append(fib(current))
        current -= 1

    fibList.reverse()
    return fibList


n = 11
assert fib_list(n) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

n = 10
assert fib_list(n) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

n = 12
assert fib_list(n) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
