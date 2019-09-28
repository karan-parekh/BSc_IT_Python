# METHOD OVERRIDING

from math import sin, radians, sqrt

class Parallelogram:
	'''class Parallelogram requires the longer side, shorter side and the smaller angle'''
	parallel_sides = True  # All the sides are parallel
	equal_sides = False	   # All the sides are NOT equal
	right_angles = False   # All the angles are NOT right angles

	def __init__(self, longer, shorter, angle):
		self.longer = longer
		self.shorter = shorter
		self.angle = angle
		self.refine_inputs()
		
	def refine_inputs(self):
		'''Makes sure the inputs provided are stored appropriately'''
		if self.longer < self.shorter:
			temp = self.longer
			self.longer = self.shorter
			self.shorter = temp
		if self.angle > 90:
			self.angle = abs(180 - self.angle)

	def area(self):
		'''Returns area'''
		height = self.shorter * sin(radians(self.angle))
		return f'Area: {self.longer * height}'

	def perimeter(self):
		'''Returns perimeter'''
		return f'Perimeter: {2 * (self.longer + self.shorter)}'

# class Rectangle inherits class Parallelogram
class Rectangle(Parallelogram):
	'''class Rectangle requires only length and breadth as inputs'''
	right_angles = True  # All the angles are right angles

	def __init__(self, length, breadth):
		super().__init__(longer=length, shorter=breadth, angle=90)

	# This area() method overrides the area() method from the Parallelorgam class
	def area(self):
		'''Returns area'''
		return f"Area: {self.longer * self.shorter}"

# class Square inherits class Rectangle which in turn inherits class Parallelogram
class Square(Rectangle):
	'''class Square requires only one side as input'''
	equal_sides = True	# All the sides are equal

	def __init__(self, side):
		super().__init__(length=side, breadth=side)


p1 = Parallelogram(8, 4, 150)
r1 = Rectangle(9, 6)
s1 = Square(7)

print(p1.parallel_sides)
print(r1.parallel_sides)
print(s1.parallel_sides)
print()
print(p1.right_angles)
print(r1.right_angles)
print(s1.right_angles)
print()
print(p1.area())
print(r1.area())
print(s1.area())
print()
print(p1.perimeter())
print(r1.perimeter())
print(s1.perimeter())