# Q2
# ---------------------------------------------------------------------
# def F2C(fahr):
#     return (5/9)*(fahr - 32)


# degF = 212

# print("Celsius: {:.2f}".format(F2C(degF)))


# Q3
# ---------------------------------------------------------------------
# numList = []
# numOfIntegers = 5

# largestOdd = 0

# while len(numList) < numOfIntegers:
#     x = float(input("integer #" + str(len(numList) + 1) + ": "))
#     if x > 0 and x.is_integer():
#         numList.append(int(x))
#         if x % 2 == 1:
#             if x > largestOdd:
#                 largestOdd = int(x)
#     else:
#         print("Positive integers, only.")

# print("Integers entered: " + str(numList))
# if largestOdd > 0:
#     print("Largest odd integer: {}.".format(largestOdd))
# else:
#     print("No odd integers entered.")

# Q4
#
# Write a function num_chars(s,c) that takes in a
# string s and a character c and returns the number
# of times that string contains that character.
# ---------------------------------------------------------------------

def num_chars(s, c):
    counter = 0
    for letter in s:
        if letter == c:
            counter += 1
    return counter


print(str(num_chars("Dwarfy MacDwarfFace", 'a')))


def num_chars_2(s, c):
    # Teaching myself list comprehensions whenever I get the chance...
    counter = sum([1 for x in s if x == c])
    return counter


print(str(num_chars_2("Dwarfy MacDwarfFace", 'a')))
