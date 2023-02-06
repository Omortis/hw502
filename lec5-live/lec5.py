import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def subsetSum(cap, myList):
    """Assumes that cap is a positive number and that myList is a list of positive numbers.
    Returns the maximum subset sum that is less than cap."""
    if cap <= 0 or myList == []:
        return 0

    first = myList[0]
    rest = myList[1:]

    if first > cap:
        return subsetSum(cap, rest)

    if first == cap:
        return cap

    if first < cap:
        # This executes the "Use it" strategy.
        useit = first + subsetSum(cap-first, rest)
        loseit = subsetSum(cap, rest)  # This executes the "Lose it" strategy.
        return max(useit, loseit)


test = [5, 10, 18, 23, 30, 45]  # , 45, 30, 23, 18, 10, 5]

# help(subsetSum1)

print(subsetSum(45, test))
print()

# test.reverse()
# print(subsetSum1(42, test))
