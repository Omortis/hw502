from functools import cache
import random
import string
import os
import numpy as np
import pandas as pd

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

UNCvDUKE = [(0, 0), (3, 0), (3, 2), (3, 4), (4, 4), (5, 4), (6, 4), (8, 4), (8, 6), (11, 6), (11, 8), (11, 11), (14, 11), (14, 13), (14, 15), (16, 15), (16, 17),
            (16, 19), (18, 19), (18, 21), (18, 22), (18, 24), (20, 24), (21, 24), (22,
                                                                                   24), (23, 24), (24, 24), (24, 26), (26, 26), (26, 28), (26, 30),
            (26, 31), (28, 31), (28, 34), (30, 34), (32, 34), (34, 34), (34, 36), (34,
                                                                                   37), (34, 39), (34, 41), (37, 41), (40, 41), (43, 41), (45, 41),
            (47, 41), (47, 44), (47, 45), (47, 47), (49, 47), (49, 49), (52, 51), (52,
                                                                                   53), (55, 53), (55, 55), (57, 55), (58, 55), (60, 55), (60, 57),
            (62, 57), (62, 59), (62, 60), (62, 61), (62, 63), (64, 63), (64, 64), (64,
                                                                                   65), (65, 65), (65, 66), (65, 67), (66, 67), (67, 67), (67, 68),
            (69, 68), (70, 68), (70, 71), (73, 71), (73, 74), (74, 74), (75, 74), (78, 74), (78, 76), (79, 76), (79, 77), (80, 77), (81, 77)]


def list2tuple(listOfTuples):
    """Function assumes that listOfTuples is a list of 2-tuples.
    Returns a 2-tuple (list1,list2) where list1 is a list of all the first tuple entries in listOfTuples
    and list2 is a list of all the second tuple entries in listOfTuples."""
    duke = []
    unc = []
    for i in listOfTuples:
        unc.append(i[0])
        duke.append(i[1])

    return (unc, duke)


testInput = [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]

assert list2tuple(testInput) == ([1, 2, 3, 4, 5, 6, 7], [1, 1, 2, 3, 5, 8, 13])
