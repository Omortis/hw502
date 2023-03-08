import os
import numpy as np
import math
import matplotlib.pyplot as plt

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def factorial(n):
    total = 1
    j = 1
    while j <= n:
        total = total*j
        j = j+1

    print("{}! = {}".format(n, total))
    return total

# n things taken r at a time


def choose(n, r):
    ans = factorial(n) / (factorial(r)*(factorial(n - r)))
    print("choose: ", ans)
    return ans


def two3sOuttaK(k):
    ans = choose(k, 2)*((1/6)**2)*math.pow(5/6, k-2)
    return ans


ans = two3sOuttaK(3)
print(ans)

ks = np.linspace(2.0, 100, 99, dtype="int")
results = []
for i in ks:
    results.append(two3sOuttaK(i))

# print(results)
fig, ax = plt.subplots()

ax.plot(ks, results, linewidth=2.0)

ax.set_xlabel('k')
ax.set_ylabel('P(X=2)')
ax.set_title("Probability of getting EXACTLY two 3s in k rolls")
plt.show()
