import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# 1. A function p(x) that returns the value 𝑥^3−10𝑥^2+5𝑥+2


def p(x):
    return x**3 - 10*x**2 + 5*x + 2

# 2. A function dp(x) that returns the value 3𝑥^2−20𝑥+5


def dp(x):
    return 3*x**2 - 20*x + 5

# 3. A function rootsOfp(startguess) that returns the solution of
#    𝑥^3−10𝑥^2+5𝑥+2=0 within .001 accuracy, by using Newton's method,
#    i.e. you start with
#       guess=startguess
#    and then update
#       guess = guess - p(guess)/dp(guess)
#    while
#       p(guess)>.001.


def rootsOfp(p, dp, guess):
    epsilon = 0.001
    numGuesses = 0
    x = guess

    while abs(p(x)) > epsilon:
        numGuesses += 1
        xi = x - p(x) / dp(x)
        x = xi

    return x


guess = 1
ans = rootsOfp(p, dp, guess)
assert abs(p(ans)) < 0.001
print("guess: ", guess)
print("ans: ", ans)
print("\tf({}) = {}".format(ans, p(ans)))

guess = -1
ans = rootsOfp(p, dp, guess)
assert abs(p(ans)) < 0.001
print("guess: ", guess)
print("ans: ", ans)
print("\tf({}) = {}".format(ans, p(ans)))

guess = 9
ans = rootsOfp(p, dp, guess)
assert abs(p(ans)) < 0.001
print("guess: ", guess)
print("ans: ", ans)
print("\tf({}) = {}".format(ans, p(ans)))
