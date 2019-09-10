# PYTHON PROGRAM TO CHECK IF THE GIVEN NUMBER IS A PALINDROME

# user input
num = int(input("Enter a number: "))

# initializing variables
temp = num  # stores backup of original number in temp 
rev_num = 0

# while loop to run until temp reduces to zero
while temp > 0:
    digit = temp % 10				# extracts the last digit
    rev_num = rev_num * 10 + digit	# stores the last digit in rev_num
    temp //= 10						# reduces temp by one digit

# output
if num == rev_num:    
    print(num, " is a palindrome")
else:
    print(num, " is not a palindrome")
