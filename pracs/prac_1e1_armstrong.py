# ARMSTRONG NUMBER
# num = int(input("Enter a number: "))
# sum = 0

def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        return True

for i in range(1, 10001):
    if is_armstrong(i):
        print(i)
        
