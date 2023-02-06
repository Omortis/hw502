import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 2: Write a function makeDict(n) that takes an integer
# input n and makes a dictionary that whose keys are the the
# strings 'key1', 'key2',...,'keyn' and whose values are
# integers n, n-1 and so on. In general keyi should have value n-i.


def makeDict(n):
    constructedDict = {}
    while n >= 0:
        constructedDict["key" + str(n)] = n
        n -= 1

    return constructedDict


testDict = {
    'key10': 10, 'key9': 9, 'key8': 8,
    'key7': 7, 'key6': 6, 'key5': 5,
    'key4': 4, 'key3': 3, 'key2': 2,
    'key1': 1, 'key0': 0
}

assert makeDict(10) == testDict
