# PYTHON PROGRAM TO REVERSE A VALUE

# user input
num = int(input("Enter a number: "))

# initializing variable
rev_num = 0

# while loop to run until number reduces to 0
while num > 0:
    digit = num % 10                # to get the last digit of the given number
    rev_num = rev_num * 10 + digit  # store that digit in rev_num variable  
    num //= 10						# floor dividing the number by 10 to get rid of the last digit
    
# output
print(rev_num)
