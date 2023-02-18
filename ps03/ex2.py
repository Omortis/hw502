import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def nDoubleFactorial(n):
    """Takes in an integer n and returns n!! 
    We assume n!! for n<=1 is 1."""
    if n <= 1:
        return 1
    else:
        return n * nDoubleFactorial(n - 2)


print(nDoubleFactorial(2))
print(nDoubleFactorial(3))
print(nDoubleFactorial(4))
print(nDoubleFactorial(5))
print(nDoubleFactorial(6))


assert nDoubleFactorial(2) == 2
assert nDoubleFactorial(3) == 3
assert nDoubleFactorial(4) == 8
assert nDoubleFactorial(5) == 15
assert nDoubleFactorial(6) == 48
