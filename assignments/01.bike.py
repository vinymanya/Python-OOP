# Bike assignment

class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	# display the bike's info
	def displayInfo(self):
		print "Price: ${}, Max_speed: {} and the total miles: {}".format(self.price, self.max_speed, self.miles)
		return self

	# display ridding
	def ride(self):
		self.miles += 10
		print "Total miles: {}".format(self.miles)
		return self
	
	# reverse
	def reverse(self):
		#What would you do to prevent the instance from having negative miles?
		if self.miles > 0:
	 		self.miles -= 5
	 	else:
	 		self.miles = 0
	 	print "Reversing {} miles".format(self.miles)
	 	return self


bike1 = Bike(200, "20mph")
bike2 = Bike(250, "35mph")
bike3 = Bike(300, "50mph")

# Chaining methods

# Have the first instance ride three times
bike1.ride().ride().ride().reverse().displayInfo()

# ride twice, reverse once and display information
bike2.ride().ride().reverse().reverse().displayInfo()

# reverse three times and display information
bike3.reverse().reverse().reverse().displayInfo()


