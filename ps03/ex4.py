import os
import math

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


def isPalindrome(s):
    """Assumes s is a str 
    Returns True if the letters in s form a palindrome;
    False otherwise. Non-letters and capitalization are ignored."""
    def toChars(s):
        t = s.lower()
        letters = ''
        for c in t:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def isPal(s):
        x = s.replace(" ", "").lower()
        srev = x[::-1]
        if x == srev:
            return True
        else:
            return False

    return isPal(toChars(s))


assert isPalindrome('Was it a cat, I saw?') == True
assert isPalindrome("Never odd or even") == True
