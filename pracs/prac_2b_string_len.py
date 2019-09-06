# PYTHON FUNCTION TO CALCULATE THE LENGTH OF A STRING

inp = input("Enter a string:")


def length(string):
	c = 0
	for x in string:
		c += 1
	return c


l = length(inp)

print("Length of the given string is: ", l)
