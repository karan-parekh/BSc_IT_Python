# PYTHON PROGRAM TO READ LAST N LINES OF A TEXT FILE

# number of lines to be read
n = 3

# open file object
file = open("lines.txt", "r")

# readlines() method returns a list of all lines in a file
lines = file.readlines()

# length of the list lines
l = len(lines)

# for loop to iterate the list
for x in range(l-n, l):
	print(lines[x], end="")

# close the file
file.close()
