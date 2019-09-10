# PYTHON PROGRAM FOR A RECURSIVE FACTORIAL FUNCTION

# user input
inp = int(input("Enter a number: "))

# returns factorial of given number
def facto(num):
	if num == 0:
		return 1				  # return 1 if the num has reduced to zero
	else:				
		f = num * facto(num - 1)  # recursivly call the function from within itself
		return f 				  # returns f at the end of recursion
 
# output
print(facto(inp))
