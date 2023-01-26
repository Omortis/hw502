import os
os.system("cls")
# os.system("clear")

# Question 4
#
# Complete the function below that takes in a temperature in Celsius
# nd returns the temperature in Fahrenheit. Use int() to make the
# output an integer. As a reminder, the formula relating Celsius and
# Fahrenheit is 𝑐=59(𝑓−32).
#
# f = (9/5)*c + 32
# ---------------------------------------------------------------------


def c_to_f(c):
    return int((9/5)*c + 32)


print(c_to_f(22))
print(c_to_f(0))
