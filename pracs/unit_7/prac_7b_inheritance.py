# PYTHON PROGRAM TO DEMONSTRATE INHERITANCE

class Employee:

	def __init__(self, name, age, pay):
		self.name = name
		self.age = age
		self.pay = pay

	def get_email(self):
		"""Returns email of the employee"""
		name = self.name.replace(" ", ".")
		email = name + "@company.com"
		return email

# class Developer inherits class Employee
class Developer(Employee):

	# __init__() method takes an additional argument of programming language
	def __init__(self, name, age, pay, prog_lang):
		super().__init__(name, age, pay)
		self.prog_lang = prog_lang

# creating instances
emp = Employee("Tom Holland", 27, 45000)
dev = Developer("Tony Stark", 33, 53000, "python")

# output
print(emp.get_email())
print(dev.get_email())
print(dev.name + " works with " + dev.prog_lang + " language")

# Note: emp and dev are an instances of class Employee and class Developer respectively
# The code demostrates that dev has access to get_email() method of class Employee, which it inherits
# Additionally, dev also has an attribute prog_lang which is only accessible in the Developer class