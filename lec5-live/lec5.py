import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def subsetSum1(cap, myList, ops=1):
    """Assumes that cap is a positive number and that myList is a list of positive numbers. 
    Attempts to return the maximum subset sum that is less than cap."""

    ops += 1
    print("ops: {}".format(ops))
    if cap <= 0 or myList == []:
        return 0

    first = myList[0]
    rest = myList[1:]

    if first > cap:
        print("{} > {}".format(first, cap))
        return subsetSum1(cap, rest, ops)

    if first == cap:
        print("{} == {}".format(first, cap))
        return cap

    if first < cap:
        print("{} < {}".format(first, cap))
        return first + subsetSum1(cap-first, rest, ops)


test = [5, 10, 18, 23, 30, 45]

# help(subsetSum1)

print(subsetSum1(42, test))
print()

test.reverse()
print(subsetSum1(42, test))
