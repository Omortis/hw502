import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def reverse(s):
    if len(s) < 1:
        return ''
    else:
        return reverse(s[1:]) + s[0]


print(reverse("fantastic"))
