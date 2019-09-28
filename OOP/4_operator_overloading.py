# Problem Statement: Mathematical addition can only be performed on int data type


class Number:

	def __init__(self, value):
		self.value = value

	def __add__(self, other):
		if type(self.value) == str:
			self.value = int(self.value)

		if type(other.value) == str:
			other.value = int(other.value)
		
		return self.value + other.value


num1 = Number('21')
num2 = Number(34)

print(num1 + num2)
