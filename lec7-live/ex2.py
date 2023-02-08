import os
import math

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# Question 2 on List Comprehension
#
# Question 2: Part A

# Using list comphrension, use one line of Python code to produce a list of integers 𝑛
# between 0 and 15 (inclusive) if and only if the 𝑛^2 − 2𝑛 + 1 is divisible by 3.

result = [n for n in range(0, 16) if (n**2 - 2*n + 1) % 3 == 0]

print(result)
assert result == [1, 4, 7, 10, 13]

# Question 2: Part B

# Store the corresponding numbers of the form 𝑛^2−2𝑛+1 that are divisble by 3 for n
# between 0 and 15, inclusive.

result = [n**2 - 2*n + 1 for n in range(0, 16) if (n**2 - 2*n + 1) % 3 == 0]

print(result)
assert result == [0, 9, 36, 81, 144]

# Question 2: Part C

# Use list comprehension to create a list of tuples (𝑛,𝑛^2−2𝑛+1)
# for those n between 0 and 15 where 𝑛2−2𝑛+1 is divisble by 3.

result = [(n, n**2 - 2*n + 1)
          for n in range(0, 16) if (n**2 - 2*n + 1) % 3 == 0]

print(result)
assert result == [(1, 0), (4, 9), (7, 36), (10, 81), (13, 144)]
