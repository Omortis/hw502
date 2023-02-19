import os
import math

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

def argTest(coeffs):

    print("coeffs     : ", coeffs)
    print("len(coeffs): ", len(coeffs))

    if len(coeffs) == 1:
        print("\tcase 1")
        return coeffs[0]

    else:
        def f(z):
            exponent = len(coeffs) - 1
            print("\tcoeffs[-1]: ", coeffs[-1])
            print("\texponent  : ", exponent)
            return coeffs[-1] * (z**exponent) + argTest(coeffs[:-1])(z)
        return f


ans = argTest([1, 2, 1])(5)
print("ans: ", ans)


# def myPoly(coeffs):
#     """coeffs is a list of floats or ints, function returns a polynomial with
#     the kth entry in coeffs as the coefficient of the monomial x^k"""
#     print("\ncoeffs: ", coeffs)

#     if len(coeffs) == 1:
#         print("+ ", coeffs[0])
#         return coeffs[0]
#     else:
#         print("last: ", coeffs[-1])
#         print(str(coeffs[-1]) + "*x**" + str(len(coeffs) - 1))
#         print("coeffs[:-1]: ", coeffs[:-1])
#         return coeffs[-1] * myPoly(coeffs[:-1])


# ans = myPoly([1, 2, 1])

# print("ans: ", ans)
