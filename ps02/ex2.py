import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 2 (3 pts): Write a function that takes in an integer 𝑛
# and returns the 𝑛-th Taylor approximation to the number 𝑒. By this
# we mean, complete the function below and use the code provided
# to sum the first 𝑛 terms of the series.
#
# Use Python based indexing, i.e. when 𝑛=0 it should return 1,
# when 𝑛=1 it should return 2, when 𝑛=2 it should return 2.5, and so on.


def factorial(n):
    total = 1
    j = 1
    while j <= n:
        total = total*j
        j = j+1
    return total


def partial_e_series(n):

    i = e = 0

    while i <= n:
        e += 1**i / factorial(i)
        i += 1

    return e


assert factorial(5) == 120
assert factorial(0) == 1
assert factorial(1) == 1

assert abs(partial_e_series(3)-2.666) <= .01
assert abs(partial_e_series(4) - 2.7083) <= .001
