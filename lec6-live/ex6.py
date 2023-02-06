import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 5 BONUS:
#
# Using the function from Exercise 4 Challenge can you compose
# these functions to compute the average of a list under all of
# it's permutations?


def listAverage(listOfLists):

    averageList = []
    for i in range(len(listOfLists[0])):
        averageList.append(0)
        for j in range(len(listOfLists)):
            averageList[i] += listOfLists[j][i]

    # averageList contains totals - need to divide to get average
    returnList = [x//len(listOfLists) for x in averageList]

    return returnList


def bruteForceReverse(inc):

    returnList = []

    for i in range(len(inc)):

        # shallow copy
        local = inc[:]
        rev = inc[:]

        returnList.append(local)
        rev.reverse()
        returnList.append(rev)

        current = inc[0]

        inc.pop(0)
        shiftList = inc[:]  # copy, not assign ref
        shiftList.append(current)
        inc = shiftList[:]

    return returnList


assert listAverage(bruteForceReverse([1, 2, 3])) == [2, 2, 2]
