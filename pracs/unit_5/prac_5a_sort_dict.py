# PYTHON PROGRAM TO SORT DICTIONARY VALUES IN ASCENDING AND DESCENDING ORDER

# initilizing dictionary of numbers
dict_num = {4: 40, 5: 50, 3: 30, 6: 60, 1: 10, 2: 20}

# storing values in a list 
value_list = list(dict_num.values())

# printing unsorted list
print("Unsorted values: ",value_list)

# sorting list
value_list.sort()

# printing sorted list
print("Sorted values:   ",value_list)
