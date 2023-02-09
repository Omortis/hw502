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


# print(derivative(f, 0.001)(.5))
# type(derivative(f, 0.001))


# Question 4: Part B

# Write a function kthDerivative(f,dx,k) that takes in a function f, a step-size dx
# and a non-negative integer k and returns the 𝑘𝑡ℎ derivative of 𝑓 with stepsize 𝑑𝑥.

# I've started this code below for you. HINT: You are free to call the derivative function above.

# explicit memoization
orderOfDerivative = 0


# def kthDerivativeRec(f, dx, k):
#     """Assumes f is a function, dx is a positive float, k is a non-negative int.
#     Returns a new function that is an approximation of the kth derivative of f, using step-size dx."""

#     if derivative(f, dx) == 0 or orderOfDerivative == k:
#         return f
#     else:
#         return derivative(f, dx)


def g(x):
    return x**4


def kthDerivative(f, dx, k):
    """Assumes f is a function, dx is a positive float, k is a non-negative int.
    Returns a new function that is an approximation of the kth derivative of f, 
    using step-size dx."""

    f_prime = derivative(f, dx)
    if k == 0:
        return f
    else:
        return kthDerivative(f_prime, dx, k-1)


print("g(10)    = {}".format(str(g(10))))

g1 = derivative(g, 0.001)
print("g'(10)   = {}".format(g1(10)))

g2 = derivative(g1, 0.001)
print("g''(10)  = {}".format(g2(10)))

g3 = derivative(g2, 0.001)
(g2, 0.001)
print("g'''(10) = {}".format(g3(10)))

print()

print("g'''(10) = {}".format(kthDerivative(g, 0.001, 3)(10)))


def h(x):
    return x**2


print("h'''(10) = {}".format(kthDerivative(h, 0.001, 4)(10)))
