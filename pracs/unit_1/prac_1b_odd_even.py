# PYTHON PROGRAM TO CHECK IF THE NUMBER IS EVEN OR ODD

# user input
num = input("Please enter a number: ")

# using modulus operator to check if the remainder is 0 i.e. if it is divisible by 2
if int(num) % 2 == 0:
    print("Entered number is an even number")
else:
    print("Entered number is an odd number")
