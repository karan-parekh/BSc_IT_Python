# RETURN TRUE FOR VOWEL, FALSE IF NOT

def is_vowel(a):
    vowels = ["a", "e", "i", "o", "u"]
    if a in vowels:
        return True
    else:
        return False

while True:
        inp = input("Enter a character: ")
        print(is_vowel(inp))
