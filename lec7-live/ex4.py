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


# Question 4: Part B

# Write a function kthDerivative(f,dx,k) that takes in a function f, a step-size dx
# and a non-negative integer k and returns the 𝑘𝑡ℎ derivative of 𝑓 with stepsize 𝑑𝑥.

# I've started this code below for you. HINT: You are free to call the derivative function above.

# explicit memoization
orderOfDerivative = 0


def kthDerivative(f, dx, k):
    """Assumes f is a function, dx is a positive float, k is a non-negative int.
    Returns a new function that is an approximation of the kth derivative of f, using step-size dx."""

    orderOfDerivative += 1

    if derivative(f, dx) == 0 or orderOfDerivative == k:
        return f
    else:
        return derivative(f, dx)


def g(x):
    return x**4


print("g(10) = {}".format(str(g(10))))
