# OOP (Object Oriented Programming)
''' 
Is used for:
	- Game Development
	- reusable code
	- Organization of code

Three main vacabularies / concepts to fully understand OOP
- Class : blueprint for creating objects
- Instance: Actual copy of the class.
- Inheritance
- Chaining

DojoStudent is a subclass of object class 
in other words DojoStudent is inheriting from the object class

'''

class DojoStudent(object):
	# Telling python how to create a Dojostudent by defining its properties
	def __init__(self, first_name, last_name, location):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location

	def greet_instructor(self):
		print "My full_name is: {} - {}".format(self.first_name, self.last_name)

	# Overwriting the method inherited from the object class
	# def __str__(self):
	# 	return "{} - {}".format(self.first_name, self.last_name)



# Creating instances of the DojoStudent
judith = DojoStudent("Judith", "Love", "Dallas")

# Self has a memory address
# <__main__.DojoStudent object at 0x10e6fa310>
# print judith

# judith.greet_instructor()

john = DojoStudent("John", "Smith", "Seattle")
# john.greet_instructor()

# print properties and methods of an instance
# print dir(john)


# Inheritance
class OnlineDojoStudent(DojoStudent):
	# Overwrite the __init__ method of the parent
	def __init__(self, first_name, last_name, location="online"):
		# Instead of repeat the properties of the parent use 'super'
		super(OnlineDojoStudent, self).__init__(first_name, last_name, location)

	# Add more methods
	# Use 'super' to overwrite a method of a parent class.
	def online_greeting(self):
		super(OnlineDojoStudent, self).greet_instructor()
		print "Greetings from the online Student!"


sarah = OnlineDojoStudent("Sarah", "West", "online")
# print sarah

sarah.online_greeting()






