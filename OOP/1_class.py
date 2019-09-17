# BASICS OF A CLASS

class User:
	"""This is a docstring for the class User.
	It can be used to write a help text and provide
	information and usage for the class"""

    # The __init__ is a special method used to initialise any class
    # The parameters passed in the init method are necessary to create an instance of that class
	def __init__(self, first, last, dob):
		self.first = first
		self.last = last
		self.dob = str(dob)		# ddmmyyyy

	def get_fullname(self):
		"""Returns the fullname of the user"""
		fullname = self.first + " " + self.last
		return fullname

	def get_dob(self):
		"""Returns dob in string format"""
		dd = self.dob[0:2]
		mm = self.dob[2:4]
		yyyy = self.dob[4:8]
		return "{}/{}/{}".format(dd, mm, yyyy)

# initialized an instance of class User called user
user = User("Tom", "Cruise", 16051988)  # dob is 16/05/1988 --> dd/mm/yyy
# 			 first	last	 dob

# prints the dob of user using get_fullname() and get_dob() methods
print(user.get_fullname(), " was born on ", user.get_dob())

# help() method displays the docstring as a summary of class User, 
# arguments expected in the init method and the description of all the methods defined in the class
help(User)
