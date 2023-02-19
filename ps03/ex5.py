import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


# def argTest(x, y):
#     print("x = {}, y = {}".format(x, y))

#     def innerArg(z):
#         return "innerArg({})".format(z)

#     return innerArg


# ans = argTest(5, 7)(6)
# print("ans: ", ans)

# def argTest(coeffs):
#     if len(coeffs) == 1:
#         def f(z):
#             return coeffs[0]
#         return f
#     else:
#         def f(z):
#             exponent = len(coeffs) - 1
#             return coeffs[-1] * (z**exponent) + argTest(coeffs[:-1])(z)
#         return f


# ans = argTest([1, 2, 1])(5)
# print("ans: ", ans)

# assert abs(argTest([1, 2, 1])(5) - 36) <= .1
# assert abs(argTest([1, 1, 1])(5) - 31) <= .1
# assert abs(argTest([1, 2, 3])(4) - 57) <= .1


def myPoly(coeffs):
    """coeffs is a list of floats or ints, function returns a polynomial with
    the kth entry in coeffs as the coefficient of the monomial x^k"""
    if len(coeffs) == 1:
        return lambda z: coeffs[0]

    else:
        exponent = len(coeffs) - 1
        return lambda z: coeffs[-1] * (z**exponent) + myPoly(coeffs[:-1])(z)


assert abs(myPoly([1, 2, 1])(5) - 36) <= .1
assert abs(myPoly([1, 1, 1])(5) - 31) <= .1
assert abs(myPoly([1, 2, 3])(4) - 57) <= .1
