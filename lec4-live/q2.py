import os

os.system("clear")

# Part 1 Write a function called triang(n) that uses recursion to return the sum
#   𝑛+(𝑛−1)+(𝑛−2) +⋯+1.

# Part 2 Add a docstring to the code of triang(n) so that when you call help(triang) it explains what the function does.


def triang(n):
    if n == 0:
        print("n == 0")
        return 0
    else:
        print("n = {}".format(n))
        return n + triang(n-1)


print(triang(5))
