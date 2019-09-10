# PYTHON PROGRAM TO CLONE A LIST

# initializing lists
list_1 = [44, 54, 22, 71, 67, 89, 20, 99]
list_2 = []  # empty list to store elements from list_1

# for loop to iterate list_1
for x in list_1:
	list_2.append(x)  # append each element (x) from list_1 to list_2 

# output
print("Original list: ", list_1)
print("Cloned list:   ", list_2)
