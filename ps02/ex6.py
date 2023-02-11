import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 6: (4 pts total, manually graded)

# Part (a): Write a function that takes in a list of n numbers
# and returns a list of all possible permutations of that list.


def factorial(n):
    total = 1
    j = 1
    while j <= n:
        total = total*j
        j = j+1
    return total


def permute(inc, result=[]):

    if len(result) == factorial(len(inc)):
        return result

    else:
        # shallow copy
        local = inc[:]
        rev = inc[:]

        result.append(local)
        rev.reverse()
        result.append(rev)

        current = inc[0]

        inc.pop(0)
        shiftList = inc[:]  # copy, not ref assign
        shiftList.append(current)
        inc = shiftList[:]
        return permute(inc, result)


ans = permute([1, 3, 5, 7])
counter = 0
for i in ans:
    print("i {}: {}".format(counter, i))
    counter += 1

# assert permute([1, 2, 3]) == [[1, 2, 3], [3, 2, 1], [
#     2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]

# Part (b): Compose the function you wrote in Part (a) with the
# function you wrote in Exercise 6 to compute the average of
# the list [1,3,5,7] under all 24 of its permutations.

# stolen from ex5.py


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
    print("averageList: ", averageList)
    returnList = [x/len(myList) for x in averageList]

    return returnList


ans = avgList(permute([1, 3, 5, 7]))

print("ans: ", ans)
