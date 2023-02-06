import os
import math

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 5: Challenge
#
# Write a function that takes in a list of 3 numbers and returns a
# list of all possible permutations of that list.
#
# You can do this by brute force and but also try using recursion. If
# you figure out a recursive solution, try to make it work for a
# list of 𝑛 numbers.


# 1, 2, 3 reverse 3, 2, 1
# shift left
# 2, 3, 1 reverse 1, 3, 2
# shift left
# 3, 1, 2 reverse 2, 1, 3


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


print("brute force: ", bruteForceReverse([1, 2, 3]))

assert bruteForceReverse([1, 2, 3]) == [[1, 2, 3], [3, 2, 1], [
    2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]


def permute(inc, result=[]):

    if len(result) == math.factorial(len(inc)):
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
        shiftList = inc[:]  # copy, not assign ref
        shiftList.append(current)
        inc = shiftList[:]
        return permute(inc, result)


print(permute([1, 2, 3]))
assert bruteForceReverse([1, 2, 3]) == [[1, 2, 3], [3, 2, 1], [
    2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]
