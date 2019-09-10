# PYTHON PROGRAM TO CHECK IF A NUMBER IS AN ARMSTRONG NUMBER

# user input
inp = int(input("Enter a number: "))

# function to return True if the number is an arstrong number
def is_armstrong(num):
    # initializing variables
    sum = 0
    temp = num              # create backup of the original number in temp

    # while loop to run until number reduces to zero
    while num > 0:          
        digit = num % 10    # to extract the last digit of the given number   
        sum += digit ** 3   # stores the addition of cube of the digit in sum
        num //= 10          # reduces the number by one digit

    # returns True if the sum matches the original number
    if temp == sum:
        return True
    else:
        return False

# output
if is_armstrong(inp):
    print("{} is an Armstrong number".format(inp))
else:
    print("{} is not an Armstrong number".format(inp))
