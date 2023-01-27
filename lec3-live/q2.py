import os
os.system("cls")
# os.system("clear")


def cube_root_ge_1(x):
    epsilon = 0.001
    left = 0
    right = x
    numGuesses = 0
    guess = (right+left)/2.0
    while abs(guess**3 - x) > epsilon:
        numGuesses += 1
        if guess**3 < x:
            left = guess
        else:
            right = guess
        guess = (right+left)/2.0
        # print("{}, {}, {}".format(left, right, guess))
    return guess


print(cube_root_ge_1(27))

# shift left to x and right to 1
# domain is limited to 0 < x < 1


def cube_root_lt_1(x):
    epsilon = 0.00001
    left = x
    right = 1
    numGuesses = 0
    guess = (right+left)/2.0
    while abs(guess**3 - x) > epsilon:
        numGuesses += 1
        if guess**3 < x:
            left = guess
        else:
            right = guess
        guess = (right+left)/2.0
        # print("{}, {}, {}".format(left, right, guess))
    return guess


print(cube_root_lt_1(0.25))


def cube_root(x):
    if x < 0:
        return "Please enter a positive number."
    elif 0 < x < 1:
        return cube_root_lt_1(x)
    elif x > 1:
        return cube_root_ge_1(x)


print(cube_root(-4))
print(cube_root(0.5))
print(cube_root(0.25))
print(cube_root(5))
