import os

os.system("clear")

# Write a function countDown(n) that uses recursion to return a string
# that counts down from n, separated by ..., ending with the base case
# where n==0, which should return Blast Off!
#
# In other words, countDown(5) should return the string
# '5...4...3...2...1...Blast Off!'.


def countDown(n, message=""):
    message += "{}...".format(n)
    if n > 0:
        n -= 1
        countDown(n, message)
    else:
        message += "Blast Off!"
        print(message)
        return message


print(countDown(5))
