import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
