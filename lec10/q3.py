import os
import numpy as np

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def random1D2D(n):
    if (isinstance(n, int) and n % 2 == 0) is not True:
        raise ValueError("Error: n must be an even integer.")
    else:
        list1 = np.random.randint(100, size=n)
        list2 = np.reshape(list1, (2, -1))
        return list1, list2


# n = 9
n = 10
list1, list2 = random1D2D(n)
print("\nlist1:")
print(list1)
print("\nlist2:")
print(type(list2))
