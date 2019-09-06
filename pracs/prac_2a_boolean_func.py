# PYTHON PROGRAM TO RETURN TRUE FOR VOWEL, FALSE IF NOT

inp = input("Enter a character: ")


def is_vowel(a):
    vowels = ["a", "e", "i", "o", "u"]
    if a in vowels:
        return True
    else:
        return False


if is_vowel(inp):
    print("{} is a vowel".format(inp))
else:
    print("{} is not a vowel".format(inp))
