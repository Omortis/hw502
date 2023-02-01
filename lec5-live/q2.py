import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# Coding Q2:
#
# Write a function that takes in two lists of integers and returns
# a single list that combines their values and is sorted from lowest to highest.

def combineAndSort(listA, listB):
    print(listA)
    print(listB)
    combinedList = listA + listB
    print(combinedList)
    combinedList.sort()
    return combinedList


a = [5, 9, 10, 32, 1]
b = [13, 12, 32, 4, 7]

print(combineAndSort(a, b))
