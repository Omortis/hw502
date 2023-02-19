import os

# linux or windows?
if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


class Accumulator(object):
    """Simple, generic accumulator for building histograms."""

    def __init__(self):
        self.__histo = {}

    def add(self, n):
        if n in self.__histo:
            self.__histo[n] += 1
        else:
            self.__histo[n] = 1

    def clear(self):
        self.histo = {}

    def __str__(self):
        output = "Accumulator:\n"
        output += "\t  n | calls\n"
        output += "\t" + ("-" * 11) + "\n"
        for n in range(0, max(self.__histo.keys()) + 1):
            output += "\t{:3} | {:3}\n".format(n, self.__histo[n])
        return output


def fib(n, accum):
    """Assumes n int>=0 Returns the n^th Fibonacci number"""

    accum.add(n)

    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1, accum) + fib(n - 2, accum)


acc = Accumulator()

n = 10
ans = fib(n, acc)
print("fib({}) = {}\n".format(n, ans))

print(acc)

acc.clear()

n = 11
ans = fib(n, acc)
print("fib({}) = {}\n".format(n, ans))

print(acc)
