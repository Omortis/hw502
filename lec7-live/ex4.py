import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Question 4 on Derivatives with Lambda Functions
# Question 4: Part A

# Modify the code below so that dx is provided as an argument. Write your new code in the code cell below!


def derivative(f, dx):
    return lambda x: (f(x+dx) - f(x))/dx


def f(x):
    return x**2


print(derivative(f, 0.001)(.5))
type(derivative(f, 0.001))


def kthDerivative(f, dx, k):
    """Assumes f is a function, dx is a positive float, k is a non-negative int.
    Returns a new function that is an approximation of the kth derivative of f, using step-size dx."""

    return None
