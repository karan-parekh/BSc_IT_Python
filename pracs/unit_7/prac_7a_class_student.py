# CLASS STUDENT TO STORE AND DISPLAY INFORMATION

class Student:

    # The __init__ is a special method used to initialise any class
    # The parameters passed in the init method are necessary to create an instance of that class
    def __init__(self, first, last, score):
        self.first = first
        self.last = last
        self.score = score

    # This method returns the fullname of the student by concatinating self.firts and self.last
    def get_fullname(self):
        fullname = self.first + " " + self.last
        return fullname
    
# initializing 2 instances of class Student
student_1 = Student('Virat', 'Kohli', 78)
student_2 = Student('Jasprit', 'Bumrah', 88)

# output
print("{} has scored {}%".format(student_1.get_fullname(), student_1.score))
print("{} has scored {}%".format(student_2.get_fullname(), student_2.score))
