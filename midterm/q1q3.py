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


# testInput = [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13)]

# assert list2tuple(testInput) == ([1, 2, 3, 4, 5, 6, 7], [1, 1, 2, 3, 5, 8, 13])


def countTies(gameData):
    """Given a list of 2-tuples, count the number of instances where the first entry equals the second entry."""
    ties = 0
    for scoreDelta in gameData:
        if scoreDelta[0] == scoreDelta[1]:
            ties += 1
    return ties


def countTies2(gameData):
    splitTeams = list2tuple(gameData)
    df = pd.DataFrame({"UNC": splitTeams[0], "Duke": splitTeams[1]})
    # skip opening score (0, 0)
    df1 = df[(df.UNC == df.Duke) & (df.UNC != 0)]
    return len(df1.index)


assert countTies2(UNCvDUKE) == 12
assert countTies([(1, 1), (2, 1), (3, 2), (4, 3),
                 (5, 5), (6, 8), (7, 13)]) == 2


def listDiff(myList):
    """Takes a list of integers of length n 
    and returns a list of integers of length n-1 
    recording the difference between each entry."""
    scoreDeltas = []
    for i in range(len(myList)):
        if i > 0:
            scoreDeltas.append(myList[i] - myList[i - 1])

    return scoreDeltas


print(listDiff([1, 2, 3, 4, 5, 6, 7]))
assert listDiff([1, 2, 3, 4, 5, 6, 7]) == [1, 1, 1, 1, 1, 1]
assert listDiff([1, 1, 2, 3, 5, 8, 13]) == [0, 1, 1, 2, 3, 5]


def ptStats(diffList):
    """Takes in a list of 0s,1s,2s, and 3s 
    and returns a tuple of the number of 0s,1s,2s, and 3s."""

    acc = {}
    for i in diffList:
        if i in acc.keys():
            acc[i] += 1
        else:
            acc[i] = 1

    # This approach only works because the range on the inputs
    # is specified.
    return (acc[0], acc[1], acc[2], acc[3])


"""Tests the answer to q3 part c"""
assert ptStats([3, 0, 0, 1, 1, 1, 2, 0, 3]) == (3, 3, 1, 2)
assert ptStats([0, 2, 0, 2, 2, 1, 0, 3, 0, 0, 0, 2]) == (6, 1, 4, 1)


# This is the DataFrame solution to Q3 part D.
teams = list2tuple(UNCvDUKE)
# print(teams)
df = pd.DataFrame(data={"UNC": ptStats(
    listDiff(teams[0])), "Duke": ptStats(listDiff(teams[1]))})
print(df)
print("\n3-pointers by team:")
print(df.loc[3, :].to_string())

# Here is the same thing without DataFrames
teams = list2tuple(UNCvDUKE)
unc = ptStats(listDiff(teams[0]))
duke = ptStats(listDiff(teams[1]))

if unc[3] > duke[3]:
    print("UNC had more 3-pointers!")
else:
    print("Duke had more 3-pointers!")
