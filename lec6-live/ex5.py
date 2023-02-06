import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 5: Challenge
#
# Write a function that takes in a list of 3 numbers and returns a
# list of all possible permutations of that list.
#
# You can do this by brute force and but also try using recursion. If
# you figure out a recursive solution, try to make it work for a
# list of 𝑛 numbers.


def listPermutations():
    return [1, 2]


# from collections.abc import Iterable


# def permute(iterable: Iterable[str]) -> set[str]:
#     perms = set()

#     if len(iterable) == 1:
#         return {*iterable}

#     for index, char in enumerate(iterable):
#         perms.update([char + perm for perm in permute(iterable[:index] + iterable[index + 1:])])

#     return perms


# if __name__ == '__main__':
#     print(permute('abc'))
#     # {'bca', 'abc', 'cab', 'acb', 'cba', 'bac'}
#     print(permute(['1', '2', '3']))
#     # {'123', '312', '132', '321', '213', '231'}
