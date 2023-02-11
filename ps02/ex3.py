import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 3 (3 pts): Write a for loop that uses the integer 𝑛
# to compute the 𝑛𝑡ℎ left hand Riemann sum of the function 𝑓(𝑥)=𝑥^2
# on the interval [0,1].

# Hint As 𝑛→∞, what should the returned sum should tend to?


def f(x):
    return x**2


def riemann_xsquared(n):
    # baked-in interval: [0, 1]
    endp1 = 0
    endp2 = 1
    delta = (endp2 - endp1) / n

    sum = i = 0

    while i < n:

        sum += f(endp1 + i*delta)*delta
        i += 1

    return sum


print("riemann_xsquared(1): ", riemann_xsquared(1))
print("riemann_xsquared(2): ", riemann_xsquared(2))
print("riemann_xsquared(3): ", riemann_xsquared(3))
print("riemann_xsquared(10): ", riemann_xsquared(10))


assert abs(riemann_xsquared(1) - 0) <= .01
assert abs(riemann_xsquared(2) - 0.125) <= .1
assert abs(riemann_xsquared(3) - 0.185185) <= .1
assert abs(riemann_xsquared(10) - 0.285) <= .01
