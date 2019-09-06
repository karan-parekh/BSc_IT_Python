# PYTHON PROGRAM TO GENERATE FIBONACCI SERIES

num = int(input("Enter a number: "))

old = 0
new = 1
count = 0

while count <= num:
    next = old + new
    print(old)
    old = new
    new = next
    count += 1
