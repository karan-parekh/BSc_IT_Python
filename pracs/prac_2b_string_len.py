# FUNCTION TO CALCULATE THE LENGTH OF A STRING

def length(string):
	c = 0
	for x in string:
		c += 1
	return c

while True:
        inp = input("Enter a string:")
        print("Length of the string is: ", length(inp))
