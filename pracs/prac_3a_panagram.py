# PYTHON PROGRAM TO CHECK IF THE STRING IS A PANAGRAM OR NOT

# user input
inp = input("Please Enter a string: ")

# function to check if the number is a panagram
def is_panagram(string):
	# initializing string of all alphabets
	alphabets = 'abcdefghijklmnopqrstuvwxyz'

	# for loop to iterate all the letters in the string alphabets
	for letter in alphabets:
		# returns Flase immediately if the letter does NOT exist in the given string
		if letter not in string:
			return False

	# returns True after the for loop is done iterating i.e. all the letters exists in the given string
	return True

# output
if is_panagram(inp):
	print("The given string is a PANAGRAM")
else:
	print("The given string is NOT a PANAGRAM")
