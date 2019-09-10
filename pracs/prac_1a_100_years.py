# PYTHON PROGRAM TO CALCULATE THE YEAR IN WHICH USER TURNS 100

# use "input" keyword to ask the user for input
name = input("Please enter your name: ")
age = input("Please enter your age: ")  

# subtracting age from current year (2019) to get birth year
birth_year = 2019 - int(age)

# adding 100 to birth year to get the 100th year
year_100 =  birth_year + 100

# output
print(name, " will turn 100 years old in the year: ") 
