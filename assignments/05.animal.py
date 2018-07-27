
# Animal class
class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	# Walk method
	def walk(self):
		self.health -= 1
		return self

	# Run method
	def run(self):
		self.health -= 5
		return self

	# Display health method
	def display_health(self):
		print "The {}'s health is: {}".format(self.name, self.health)
		return self

# Create animal instances
animal1 = Animal("cat", 50)
animal1.walk().walk().walk().run().run().display_health()


# Subclass that inherits from parent Animal class.
class Dog(Animal):
	def __init__(self, name, health=150):
		super(Dog, self).__init__(name, health)

	# pet method
	def pet(self):
		self.health += 5
		return self

# Create instances of the Dog class
milou = Dog("Dog")
# Chaining methods
milou.walk().walk().walk().run().run().pet().display_health()


# Another Subclass that inherits from parent Animal class.
class Dragon(Animal):
	def __init__(self, name, health=170):
	 	super(Dragon, self).__init__(name, health)

	# Fly method
	def fly(self):
	 	self.health -= 10
	 	return self
	# Display health emthod
	def displayHelath(self):
	 	super(Dragon, self).display_health()
	 	print "I am a Dragon!"

# Create a new instance
dragon1 = Dragon("Dragon")
dragon1.fly().displayHelath()



