# PYTHON PROGRAM TO READ A TEXT FILE

# variable to store the file object
file = open('python.txt', 'r')

# read and store file contents
contents = file.read()

# output
print(contents)

# close opened file
file.close()