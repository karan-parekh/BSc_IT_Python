# PYTHON PROGRAM FOR A RECURSIVE FACTORIAL FUNCTION

inp = int(input("Enter a number: "))


def facto(num):
	if num == 0:
		return 1
	else:
		f = num * facto(num - 1)
		return f


print(facto(inp))