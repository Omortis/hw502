import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def list_reverse(s):
    try:
        reversed = [0] * len(s)
        for i in range(len(s)):
            reversed[len(s) - 1 - i] = s[i]
        return reversed
    except TypeError as msg:
        print("Arg must be a list: ", msg)
        return []


datum = [i for i in range(20)]
ans = list_reverse(datum)
assert ans == [19, 18, 17, 16, 15, 14, 13,
               12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
