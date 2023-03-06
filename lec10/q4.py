import os
import numpy as np

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# uDist1 = np.random.randint(-1, 2, 20, int)
# print(uDist1)

# # numpy.random.randint docs specify this method for new code[1]:
# rng = np.random.default_rng()
# uDist2 = rng.integers(-1, 2, 20, int)
# print(uDist2)

n = 100
d = 500

rng = np.random.default_rng()
newList = [rng.integers(-1, 2, n, int).sum() for x in np.zeros(d)]
print(newList)
