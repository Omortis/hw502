import os

os.system("clear")

# Write a function countDown(n) that uses recursion to return a string
# that counts down from n, separated by ..., ending with the base case
# where n==0, which should return Blast Off!
#
# In other words, countDown(5) should return the string
# '5...4...3...2...1...Blast Off!'.


def countDown(n):
    if n == 0:
        return "Blast Off!"
    else:
        return str(n) + "..." + countDown(n-1)


print(countDown(5))
