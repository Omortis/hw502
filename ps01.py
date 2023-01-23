import os
os.system("cls")
# os.system("clear")

# Question 3
#
# Finish the function below that takes in the length of the two parallel
# sides of a trapezoid 𝑎 and 𝑏, which are separated by a distance h,
# and returns its area.
#
# Area of a trapezoid A = (h/2)(a + b)
# ---------------------------------------------------------------------


# def area_of_trapezoid(a, b, h):
#     return (h / 2)*(a + b)


# print(area_of_trapezoid(3, 3, 5))
# print(area_of_trapezoid(3, 4, 5))

# Question 4
#
# Complete the function below that takes in a temperature in Celsius
# nd returns the temperature in Fahrenheit. Use int() to make the
# output an integer. As a reminder, the formula relating Celsius and
# Fahrenheit is 𝑐=59(𝑓−32).
#
# f = (9/5)*c + 32
# ---------------------------------------------------------------------


# def c_to_f(c):
#     return int((9/5)*c + 32)


# print(c_to_f(22))
# print(c_to_f(0))

# Question 5
#
# Complete the function below that takes an integer as input and outputs
# whether or not the number is odd or even. Make sure you have an output
# that prints "The number x is even/odd", where 𝑥 was the input.
# ---------------------------------------------------------------------

# no need to check the sign (-4 / 2 = -2 so -4 is even)


# def even_or_odd(x):
#     if x % 2 > 0:
#         return "The number {} is odd.".format(x)
#     else:
#         return "The number {} is even.".format(x)


# even_or_odd(12)

# Question 6
#
# Write a Python function draw(n) that constructs the following pattern
# using the print function and a nested for loop. Here is what the
# output should look like for 𝑛=5, but with less space between lines.
# ---------------------------------------------------------------------


# def draw_2(n):
#     adder = 1
#     y = 1
#     for x in range((2 * n) - 1):
#         print('*' * y)
#         if x >= n-1:
#             adder = -1
#         y += adder


# draw_2(5)

# Question 7
# Write a function that takes in an integer 𝑛 and computes 𝑛!. Do this
# without recursion.
# ---------------------------------------------------------------------


def factorial_iter(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(factorial_iter(6))
print(factorial_iter(7))
print(factorial_iter(10))
