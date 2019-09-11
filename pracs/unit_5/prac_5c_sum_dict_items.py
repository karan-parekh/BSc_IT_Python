# PYTHON PROGRAM TO CONCATENATE ITEMS IN A DICTIONARY

# initilizing dictionary of numbers
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# initializing variables
key_sum = 0		# to store sum of keys
value_sum = 0	# to store sum of values

# for loop to itrate two variables: k and v, over items in dict_num
for k, v in dict_num.items():
	key_sum += k 	# increment key_sum by k 
	value_sum += v 	# increment value_sum by v

# new dictionary to store sum of all items in dict_num
dict_sum = {key_sum: value_sum}

# output
print(dict_sum)
