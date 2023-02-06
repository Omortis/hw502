import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 1: Write a function count_overlapping(intervals,point) takes
# in a list of closed intervals [[a_0,b_0],[a_1,b_1],...] and a value
# point and outputs how many of the closed intervals contain the point.


def count_overlapping(intervals, point):
    print("intervals:")
    print(intervals)
    print("point:")
    print("{}: {}, {}".format(point, point[0], point[1]))

    closedIntervalHits = 0
    for interval in intervals:
        if interval[0] <= point[0] and interval[1] >= point[1]:
            closedIntervalHits += 1

    return closedIntervalHits


print("count_overlapping: ", count_overlapping([[0, 1], [1, 5]-], (2, 3)))
