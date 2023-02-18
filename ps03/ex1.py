import os
import matplotlib.pyplot as plt
import numpy as np

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def fib(n):
    """Assumes n int>=0
       Returns the n^th Fibonacci number"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# print(fib(13))


def gen_Fib(n, m, k):
    """Takes in 3 integers n, m, k and 
    returns the kth element of the generalized Fibonacci sequence 
    that starts as ...0,n,m,n+m, n+2m,"""

    # k = 2 and k = 1 are just n and m, respectively, so stop at 2
    if k == 2:
        return m
    else:
        # print("n = {}, m = {}, k = {}".format(n, m, k))
        return gen_Fib(m, n+m, k - 1)


ans = gen_Fib(1, 1, 7)
print(ans)

assert gen_Fib(1, 1, 7) == 13
assert gen_Fib(1, 1, 10) == 55
assert gen_Fib(1, 3, 5) == 11
assert gen_Fib(1, 3, 10) == 123
assert gen_Fib(1, -1, 8) == -5
