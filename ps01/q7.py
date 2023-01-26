import os
os.system("cls")
# os.system("clear")

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
