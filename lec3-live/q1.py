import os
os.system("cls")
# os.system("clear")


def sqrt_ge_1(x):
    epsilon = 0.001
    left = 0
    right = x
    numGuesses = 0
    guess = (right+left)/2.0
    while abs(guess**2 - x) > epsilon:
        numGuesses += 1
        if guess**2 < x:
            left = guess
        else:
            right = guess
        guess = (right+left)/2.0
        # print("{}, {}, {}".format(left, right, guess))
    return guess


sqrt_ge_1(5)

# shift left to x and right to 1
# domain is limited to 0 < x < 1


def sqrt_lt_1(x):
    epsilon = 0.00001
    left = x
    right = 1
    numGuesses = 0
    guess = (right+left)/2.0
    while abs(guess**2 - x) > epsilon:
        numGuesses += 1
        if guess**2 < x:
            left = guess
        else:
            right = guess
        guess = (right+left)/2.0
        # print("{}, {}, {}".format(left, right, guess))
    return guess


sqrt_lt_1(0.25)


def sqrt(x):
    if x < 0:
        return "Please enter a positive number."
    elif 0 < x < 1:
        return sqrt_lt_1(x)
    elif x > 1:
        return sqrt_ge_1(x)


print(sqrt(-4))
print(sqrt(0.5))
print(sqrt(0.25))
print(sqrt(5))
