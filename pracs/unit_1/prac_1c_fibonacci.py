# PYTHON PROGRAM TO GENERATE FIBONACCI SERIES

# user input
num = int(input("Enter a number: "))

# initializing variables
old = 0  
new = 1
count = 0

# while loop to run until counter reaches the given number
while count <= num:
    next = old + new
    print(old)
    old = new
    new = next
    count += 1
