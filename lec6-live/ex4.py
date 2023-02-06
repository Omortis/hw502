import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 4: Write a function that takes in a list of lists of
# equal length and then produces their average list, i.e. this
# is a list where the entry in index [i] is the average of all
# the given entries in index [i].


def listAverage(listOfLists):

    averageList = []
    for i in range(len(listOfLists[0])):
        averageList.append(0)
        for j in range(len(listOfLists)):
            averageList[i] += listOfLists[j][i]

    # averageList contains totals - need to divide to get average
    returnList = [x//len(listOfLists) for x in averageList]

    return returnList


listOfLists = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

returnedList = [(1 + 6 + 11)/3, (2 + 7 + 12)/3,
                (3 + 8 + 13)/3, (4 + 9 + 14)/3, (5 + 10 + 15)/3]

print(returnedList)
assert listAverage(listOfLists) == returnedList
