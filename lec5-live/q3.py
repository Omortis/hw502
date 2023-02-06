import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def reverse(s, ops=0):
    ops += 1
    print("ops: {}".format(ops))
    if len(s) > 1:
        return reverse(s[1:], ops) + s[0]
    else:
        return s[0]


print("modified")
print(reverse("fantastic"))
print()


def reverse_orig(s, ops=0):
    ops += 1
    print("ops: {}".format(ops))
    if len(s) == 0:
        return ''
    else:
        return reverse(s[1:], ops) + s[0]


print("original")
print(reverse_orig("fantastic"))
