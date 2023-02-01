import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def subsetSum(cap, myList):
    """Assumes that cap is a positive number and that myList is a list of positive numbers. 
    Returns the maximum subset sum that is less than cap."""

    print(myList)
    if cap <= 0 or myList == []:
        return 0

    first = myList[0]
    rest = myList[1:]

    if first > cap:
        # print("first: {} > cap: {}".format(first, cap))
        return subsetSum(cap, rest)

    elif first == cap:
        # print("first: {} == cap: {}".format(first, cap))
        return cap

    else:  # first < cap:
        # This executes the "Use it" strategy.
        useit = first + subsetSum(cap-first, rest)
        # This executes the "Lose it" strategy.
        loseit = subsetSum(cap, rest)
        # print("\nfirst: {} < cap: {}".format(first, cap))
        # print("useit: {} < loseit: {}".format(useit, loseit))
        return max(useit, loseit)


help(subsetSum)

print(subsetSum(42, [5, 10, 18, 23, 30, 45]))

print()
print(subsetSum(42, [45, 30, 23, 18, 10, 5]))
