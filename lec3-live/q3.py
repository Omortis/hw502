import os

os.system("cls")
# os.system("clear")

# user defined function and first derivative


def p(x):
    return x**3 - 10*x**2 + 5*x + 2


def p_prime(x):
    return 3*x**2 - 20*x + 5


def newton_raphson(p, p_prime):
    epsilon = 1E-15
    numGuesses = 0
    guess = 0
    x = guess

    while abs(p(x)) > epsilon:
        numGuesses += 1
        xi = x - p(x) / p_prime(x)
        print("Iteration {}, x {:.2f}, p {}, p_prime {}".format(
            numGuesses, x, p(x), p_prime(x)))
        x = xi

    return x


root = newton_raphson(p, p_prime)
print("root: {}".format(root))
print("p({}) = {}".format(root, p(root)))
