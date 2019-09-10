# PYTHON FUNCTION TO CALCULATE THE LENGTH OF A STRING

# user input
inp = input("Enter a string:")

# function returns length of the given string
def length(string):
	# initializing counter variable
	count = 0

	# iterate over the given string
	for x in string:
		count += 1	# increment counter for each variable in the string
	return count 	# return counter after the loop ends

# function call
l = length(inp)

# output
print("Length of the given string is: ", l)
