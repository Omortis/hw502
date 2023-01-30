import os

os.system("clear")

# Q3: Printing a string backwards and other tricks

# For this problem, assume that you only know the following and a little bit of recursion.

#     You can concatenate two strings using the + operation.
#     If you want to know the length of a string s, you can use the command len(s).
#     If you want to access the 𝑖𝑡ℎ
#     entry in a string, you can use s[i]. Note that this starts counting at 0.
#     The command s[i:j] returns the substring starting at entry number i and ends at j-1.

# Use recursion to write a function printBackwards(x) that takes in a string and prints it backwards.


def printBackwards(x):
    # base case
    if len(x) == 1:
        return x
    else:
        strLen = len(x)
        return x[strLen-1] + printBackwards(x[0:strLen - 1])


ans = printBackwards("fantastic")
print(ans)
