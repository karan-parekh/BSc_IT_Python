# INHERITANCE

class User:
	"""User is a class to store and process user data such as name and dob"""
	admin = False  # admin is a class variable, availabe to all the methods in User and Developer

	def __init__(self, first, last):
		self.first = first
		self.last = last

	def get_fullname(self):
		"""Returns the fullname of the user"""
		fullname = self.first + " " + self.last
		return fullname

# Developer inherits all the methods and attributes from class User 
class Developer(User):
	admin = True  # this class variable is only available to methods in Developer class

	def __init__(self, first, last, prog_lang):
		super().__init__(first, last)  # super() method is used to inherit the init method from the parent class
		self.prog_lang = prog_lang

# help() displays the Method Resolution Order 
# which is the order in which the iterpreter looks for methods and attributes
print(help(Developer))

# creating instances
user_1 = User("Tom", "Cruise")
user_2 = Developer("David", "Blane", "Python")

for user in [user_1, user_2]:
	if user.admin:
		print("Access Granted to user: ", user.get_fullname())
	else:
		print("Access Denied to user:  ", user.get_fullname())
