# PYTHON PROGRAM TO CHECK IF THE GIVEN NUMBER IS A PALINDROME

num = int(input("Ennter a number: "))
temp = num
rev_num = 0

while temp > 0:
    digit = temp % 10
    rev_num = rev_num * 10 + digit
    temp //= 10

if num == rev_num:    
    print(num, " is a palindrome")
else:
    print(num, " is not a palindrome")
