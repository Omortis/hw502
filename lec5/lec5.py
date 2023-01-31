import os

os.system("clear")


def subsetSum1(cap, myList):
    """Assumes that cap is a positive number and that myList is a list of positive numbers. 
    Attempts to return the maximum subset sum that is less than cap."""
    if cap <= 0 or myList == []:
        return 0

    first = myList[0]
    rest = myList[1:]

    if first > cap:
        print("{} > {}".format(first, cap))
        return subsetSum1(cap, rest)

    if first == cap:
        print("{} == {}".format(first, cap))
        return cap

    if first < cap:
        print("{} < {}".format(first, cap))
        return first + subsetSum1(cap-first, rest)


test = [5, 10, 18, 23, 30, 45]


print(subsetSum1(42, test))
