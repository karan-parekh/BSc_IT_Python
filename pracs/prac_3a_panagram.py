# PYTHON PROGRAM TO CHECK IF THE STRING IS A PANAGRAM OR NOT
inp = input("Please Enter a string: ")

def is_panagram(string):
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	for letter in alphabets:  # for loop to iterate all the letters in the string alphabets
		if letter not in string:  # returns Flase immediately if the letter does not exist in the given string
			return False
	return True  # returns True after the for loop is done iterating i.e. all the letters exists in the given string

if is_panagram(inp):
	print("The given string is a PANAGRAM")
else:
	print("The given string is NOT a PANAGRAM")
