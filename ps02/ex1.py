import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 1 (2 pts): Complete the function below that takes
# in three integers (𝑎,𝑏,𝑐) and returns the number of integers
# between 𝑎 and 𝑏 (inclusive of the endpoints) that are
# divisible by 𝑐. Make sure it tests 𝑎 and 𝑏 for divisibility by 𝑐!


def inclusive_list(a, b):
    # handle signed endpoints
    endp1 = a if a < b else b
    endp2 = b if a < b else a

    # create list from endpoints
    intList = [endp1]
    while endp1 < endp2:
        endp1 += 1
        intList.append(endp1)

    return intList


assert inclusive_list(10, 20) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
assert inclusive_list(-5, 20) == [-5, -4, -3, -2, -1, 0, 1, 2, 3,
                                  4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
assert inclusive_list(20, -5) == [-5, -4, -3, -2, -1, 0, 1, 2, 3,
                                  4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def how_many_divisible(a, b, c):
    counter = 0
    interval = inclusive_list(a, b)
    for x in interval:
        counter += 1 if x % c == 0 else 0

    return counter


assert how_many_divisible(20, -5, 5) == 6
assert how_many_divisible(20, -4, 5) == 5
assert how_many_divisible(10, 20, 5) == 3
assert how_many_divisible(30, 77, 7) == 7
