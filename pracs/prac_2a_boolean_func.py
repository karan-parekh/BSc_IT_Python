# PYTHON PROGRAM TO RETURN TRUE FOR VOWEL, FALSE IF NOT

# user input
inp = input("Enter a character: ")

# function to check if the given string is a vowel 
def is_vowel(a):
	# initializing vowel list
    vowels = ["a", "e", "i", "o", "u"]
    
    # returns True if the string exists in the list of vowels
    if a in vowels:
        return True
    else:
        return False

# output
if is_vowel(inp):
    print("{} is a vowel".format(inp))
else:
    print("{} is not a vowel".format(inp))
