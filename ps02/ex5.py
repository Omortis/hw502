import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 5 (2 pts): Write a function that takes in a list of
# lists of equal length and then produces their average list,
# i.e. this is a list where the entry in index i is the average
# of all the given entries in index i.


def avgList(myList):
    """Assumes the argument myList is a list of lists, 
    all of the same length k with int or float entries. 
    Returns a list of length k that computes the entrywise average."""
    averageList = []
    for i in range(len(myList[0])):
        averageList.append(0)
        for j in range(len(myList)):
            averageList[i] += myList[j][i]

    # averageList contains totals - need to divide to get average
    returnList = [x/len(myList) for x in averageList]

    return returnList


listOfLists = [[3, 5, 7, 8], [1, 4, 6, 8]]

print(avgList(listOfLists))

test1 = [2.0, 4.5, 6.5, 8.0]
for j in [abs(test1[i] - avgList([[3, 5, 7, 8], [1, 4, 6, 8]])[i]) < .1 for i in range(4)]:
    assert j
test2 = [2.0, 2.0, 2.0]
for j in [abs(test2[i] - avgList([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])[i]) < .1 for i in range(3)]:
    assert j
