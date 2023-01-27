import os
os.system("cls")
# os.system("clear")

# Question 6
#
# Write a Python function draw(n) that constructs the following pattern
# using the print function and a nested for loop. Here is what the
# output should look like for 𝑛=5, but with less space between lines.
# ---------------------------------------------------------------------


def draw(n):
    adder = 1
    y = 1
    for x in range((2 * n) - 1):
        for i in range(y):
            print("*", end="")
        print()
        if x >= n-1:
            adder = -1
        y += adder


draw(5)


def draw_2(n):
    adder = 1
    y = 1
    for x in range((2 * n) - 1):
        print('*' * y)
        if x >= n-1:
            adder = -1
        y += adder


draw_2(5)
