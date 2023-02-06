import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def subsetSum(cap, myList, ops=0):
    """Assumes that cap is a positive number and that myList is a list of positive numbers. 
    Returns the maximum subset sum that is less than cap."""

    ops += 1
    print("ops: {}".format(ops))

    # print(myList)
    if cap <= 0 or myList == []:
        return 0

    first = myList[0]
    rest = myList[1:]

    if first > cap:
        return subsetSum(cap, rest, ops)

    if first == cap:
        return cap

    if first < cap:
        # This executes the "Use it" strategy.
        useit = first + subsetSum(cap-first, rest, ops)
        # This executes the "Lose it" strategy.
        loseit = subsetSum(cap, rest, ops)
        return max(useit, loseit)


print(subsetSum(42, [5, 10, 18, 23, 30, 45]))  # , 45, 30, 23, 18, 10, 5]))

# print()
# print(subsetSum(42, [45, 30, 23, 18, 10, 5]))
