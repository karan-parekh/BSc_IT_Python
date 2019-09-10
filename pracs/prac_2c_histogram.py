# PYTHON PROGRAM TO PRINT HISTOGRAM FOR GIVEN LIST

# initializing list of vlaues
values = [4, 7, 4, 2]

# for loop to iterate for each number in the list of vlaues 
for v in values:
	# for loop to print "#" for v number of times
	for x in range(v):
		print("#", end="") 
	print()  # for new line
