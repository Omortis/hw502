import os
import math

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Finger Exercise:

# Use list comprehension to make a list that has the entries as all possible sums
# of the elements in the lists [3, 5, 6] and [10, 13, 27], i.e. [13, 16, 30, 15, 18, 32, 16, 19, 33]


def sumList(list1, list2):

    result = []

    for i in list1:
        for j in list2:
            result.append(i + j)

    return result


list1 = [3, 5, 6]
list2 = [10, 13, 27]
expected = [13, 16, 30, 15, 18, 32, 16, 19, 33]

x = sumList(list1, list2)

print(x)
assert x == expected
