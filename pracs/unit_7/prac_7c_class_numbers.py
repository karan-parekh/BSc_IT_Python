
class Numbers:
	MULTIPLIER = 3

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self):
		return self.x + self.y

	def multiply(self, a):
		return a * self.MULTIPLIER

	@staticmethod
	def subtract(b, c):
		return b - c

	@property
	def value(self):
		return (self.x, self.y)

	@value.setter
	def value(self, t):
		self.x = t[0]
		self.y = t[1]

	@value.deleter
	def value(self):
		self.x = None
		self.y = None

num = Numbers(4, 6)

# adding numbers
print(num.add())

# multiplying with the MULTIPLIER
print(num.multiply(2))

# subtracting
print(num.subtract(5, 3))

# original values
print("Original values: ", num.value)

# setting values
num.value = (7, 9)
print("     New values: ", num.value)

# deleting values
del num.value
print(num.value)
