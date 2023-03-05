import os
import math
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# ---------------------------------------------------------------------
# Q1
# ---------------------------------------------------------------------


# def f(x):
#     return math.exp(x)


# x = list(range(0, 10))

# y = []
# for i in x:
#     y.append(f(i))

# fig, ax = plt.subplots()

# ax.plot(x, y, color="green")

# ax.set_xlabel("Time", fontsize = 16)
# ax.set_ylabel("Growth", fontsize = 16)
# ax.set_title("y = exp(x)", fontsize = 18, color = "darkblue")
# plt.grid(True, linestyle='--')

# plt.show()


# ---------------------------------------------------------------------
# Q2
#
# Make a scatter plot with the points [(1,3), (2,4), (3,1)] labelled "My Scatter Plot"
# ---------------------------------------------------------------------

x = [1, 2, 3]
y = [3, 4, 1]

fig, ax = plt.subplots()

ax.scatter(x, y)
ax.set_title("My Scatter Plot")
plt.grid(True, linestyle='--')
plt.show()
