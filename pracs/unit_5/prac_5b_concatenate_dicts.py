# PYTHON PROGRAM TO CONCATENATE DICTIONARIES

# initializing dictionaries
dict_1 = {1: 10, 2: 20}
dict_2 = {3: 30, 4: 40}
dict_3 = {5: 50, 6: 60}
new_dict = {}	# empty dictionary to store concatenated dictionaries

# list of all dictionaries
dict_list = [dict_1, dict_2, dict_3]

# for loop to iterate all dictionaries in the list
for d in dict_list:
	new_dict.update(d)

# output
print(new_dict)