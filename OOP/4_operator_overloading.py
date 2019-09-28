# Problem Statement: Mathematical addition can only be performed on int data type and not str
# Overload the + operator to accept any numerical data types and return the addition in int 

class Number:
	"""class Number performs Add(+) operation on any numerical data types including str"""

	def __init__(self, value):
		self.value = value

	# Overloads the + operator to perform the actions below
	def __add__(self, other):
		left = self
		right = other

		# coverts to int if the value of the left operand is not of type int
		if type(left.value) is not int:
			left.value = int(left.value)

		# coverts to int if the value of the right operand is not of type int
		if type(right.value) is not int:  
			right.value = int(right.value)
		
		return left.value + right.value


num1 = Number('21')
num2 = Number(34.2)

print(num1 + num2)
