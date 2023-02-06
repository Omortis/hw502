import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 1: Write a function count_overlapping(intervals,point) takes
# in a list of closed intervals [[a_0,b_0],[a_1,b_1],...] and a value
# point and outputs how many of the closed intervals contain the point.


def count_overlapping(intervals, point):
    closedIntervalHits = 0
    for interval in intervals:
        if interval[0] <= point[0] and interval[1] >= point[1]:
            closedIntervalHits += 1

    return closedIntervalHits


point = (2, 3)
intervals1 = [[0, 1], [1, 5], [5, 8], [-1, 10]]
intervals2 = [[0, 1], [1, 5], [2, 8], [-1, 10]]
intervals3 = [[0, 11], [1, 5], [5, 8], [-1, 10]]

assert count_overlapping(intervals1, point) == 2
assert count_overlapping(intervals2, point) == 3
assert count_overlapping(intervals3, point) == 3
