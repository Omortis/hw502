import os
os.system("cls")
# os.system("clear")

# Question 5
#
# Complete the function below that takes an integer as input and outputs
# whether or not the number is odd or even. Make sure you have an output
# that prints "The number x is even/odd", where 𝑥 was the input.
# ---------------------------------------------------------------------

# no need to check the sign (-4 / 2 = -2 so -4 is even)


def even_or_odd(x):
    if x % 2 > 0:
        return "The number {} is odd.".format(x)
    else:
        return "The number {} is even.".format(x)


even_or_odd(12)
