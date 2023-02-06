import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Exercise 3: How might you generalize the Hamming distance, let's
# call it the substitution distance between two strings of unequal length?


def substitution_distance(s1, s2):
    """Assumes s1 and s2 are strings of the same length and returns their Hamming Distance"""

    # Change counter to default to the "cost" of the missing characters
    counter = abs(len(s1) - len(s2))
    # Safety: pick the shorter string to call range() upon and avoid the IndexError
    shorter = s1 if len(s2) >= len(s1) else s2

    for i in range(len(shorter)):
        if s1[i] != s2[i]:
            counter = counter + 1
    return counter


s1 = 'cats'
s2 = 'dogs'
s3 = 'spam'
s4 = 'spa'
s5 = 'aloud'
s6 = 'loud'
s7 = 'alien'
s8 = 'sales'

assert substitution_distance(s5, s8) == 5  # aloud, sales
assert substitution_distance(s2, s3) == 4  # dogs, spam
assert substitution_distance(s3, s4) == 1  # spam, spa
assert substitution_distance(s1, s4) == 4  # cats, spa
assert substitution_distance(s4, s5) == 5  # spa, aloud
