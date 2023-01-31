import os

os.system("clear")

# Q4: Primality

# Write a function isPrime that takes in an integer n and
# returns whether it is prime or not by recursively checking
# divisibility by integers between 2 and 𝑛/2

# .

# HINT: Use two arguments, where the second argument is the number y
# ou're checking divisibility by. Give this one a default value as
# in the code below.

# def isPrime(n,i=2):
#     if i> n/2:
#         return True
#     # Your Solution here

# Use the test function below to make sure your function does what's intended.


def isPrime(n, i=2):
    # print("outer, n = {},  i = {}".format(n, i))
    if i > n/2:
        # print("i > n/2")
        return True
    else:
        if n % i == 0:
            # print("\tmod = 0, n = {}, i = {}".format(n, i))
            return False
        else:
            # print("\tmod != 0, n = {}, i = {}".format(n, i))
            return isPrime(n, i+1)


def testisPrime(n):
    for i in range(n+1):
        print('It is ', isPrime(i), 'that', i, 'is prime.')


testisPrime(19)
