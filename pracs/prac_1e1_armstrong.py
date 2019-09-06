# PYTHON PROGRAM TO CHECK IF A NUMBER IS AN ARMSTRONG NUMBER
num = int(input("Enter a number: "))
sum = 0


def is_armstrong(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if n == sum:
        return True


if is_armstrong(num):
    print("{} is an Armstrong number".format(num))
else:
    print("{} is not an Armstrong number".format(num))
