# PYTHON PROGRAM TO RETURN TRUE IF TEHRE IS AT LEAST ONE COMMON ELEMENT IN TWO LISTS

# initializing two lists
list_1 = [44, 44, 22, 71, 67, 89, 20, 99]
list_2 = [93, 68, 17, 49, 20, 12, 57, 10]

# function to return True if there exists a common element in the lists else False
def is_common_element(l1, l2):
	# for loop to iterate over list 1
	for element in l1:
		if element in l2:	# return True immediately if a common element is found
			return True

	# retunr False after the loop ends and no common element is found
	return False

# output
if is_common_element(list_1, list_2):
	print("There exists at least one common element in the lists")
else:
	print("No common element found")
