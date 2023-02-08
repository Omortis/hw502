import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# Question 3 on Multiple List Comprehension

# Use list comprehension to make a list that has the entries as all
# possible sums of the elements in the lists [3, 5, 6] and [10, 13, 27],
# i.e. [13, 16, 30, 15, 18, 32, 16, 19, 33]

def sumList(list1, list2):

    result = []

    for i in list1:
        for j in list2:
            result.append(i + j)

    return result

# result = [n for n in range(0, 16) if (n**2 - 2*n + 1) % 3 == 0]


a = [3, 5, 6]
b = [10, 13, 27]

result = [x + y for x in a for y in b]

print(result)
assert result == [13, 16, 30, 15, 18, 32, 16, 19, 33]
