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


# def list_reverse(s):
#     try:
#         reversed = [0] * len(s)
#         for i in range(len(s)):
#             reversed[len(s) - 1 - i] = s[i]
#         return reversed
#     except TypeError as msg:
#         print("arg must be a list: ", msg)
#         return None


# datum = [i for i in range(20)]
# assert list_reverse(datum) == [19, 18, 17, 16, 15, 14, 13,
#                                12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# assert list_reverse("cat") == ['t', 'a', 'c']
# assert list_reverse(5) == None


# ---------------------------------------------------------------------
# Q2
# ---------------------------------------------------------------------
# def int_sum(x, y):
#     try:
#         if x % 2 == 0 and y % 2 == 0:
#             return x * y
#         else:
#             return x + y
#     except TypeError as msg:
#         print("args must be integers: ", msg)
#         return None


# assert int_sum(4, 6) == 24
# assert int_sum(4, 5) == 9
# assert int_sum(5, 7) == 12
# assert int_sum(5, 6) == 11
# assert int_sum("ham", "cheese") == None

# ---------------------------------------------------------------------
# Q3
# ---------------------------------------------------------------------


# def int_finder(L, m):
#     try:
#         df = pd.DataFrame(L)
#         return df.value_counts()[m]
#     except ValueError as msg:
#         print("args must be a list of integers, followed by a single integer")
#         return None


# assert int_finder([1, 23, 4, 2, 56, 7, 6, 2, 2, 2], 2) == 4
# assert int_finder("cat", 2) == None


# def int_finder2(L, m):
#     try:
#         count = L.count(m)
#         return count
#     except TypeError as msg:
#         print("args must be a list of integers, followed by a single integer")
#         return None


# assert int_finder2([1, 23, 4, 2, 56, 7, 6, 2, 2, 2], 2) == 4
# assert int_finder2("cat", 2) == None

# ---------------------------------------------------------------------
# Q4
# ---------------------------------------------------------------------
# def uniq(L):
#     newList = np.unique(L).tolist()
#     return newList


# assert uniq([1, 2, 32, 14, 2, 1]) == [1, 2, 14, 32]

# ---------------------------------------------------------------------
# Q5
# ---------------------------------------------------------------------
import string
import random


# def pick_random(l):
#     try:
#         return l[random.randrange(len(l))]
#     except TypeError as msg:
#         print("arg must be a list of any type")
#         return None


# alphabet = list(string.ascii_lowercase)
# print("alphabet: ", alphabet)
# ans = pick_random(alphabet)
# print("ans: ", ans)

# assert pick_random(1) == None

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
