# PYTHON PROGRAM TO REMOVE 0th, 2nd, 4th AND 5th ELEMENTS OF A LIST

# initializing lists
# indices  0   1   2   3   4   5   6   7
numbers = [44, 54, 22, 71, 67, 89, 20, 99]
indices = [0, 2, 4, 5]  # list of indices to be deleted
elements = []			# empty list to store elements of indices

# print list before deletion of elements
print("Original list: ", numbers)

# for loop to store elements of indices from numbers
for i in indices:
	elements.append(numbers[i])

# for loop to remove elements from numbers
for e in elements:
	numbers.remove(e)

# output
print("Modified list: ", numbers)
