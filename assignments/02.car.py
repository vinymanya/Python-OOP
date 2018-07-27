# Car class
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0.12
		
		if self.price > 10000:
			self.tax = 0.15

		self.display_all()


	# Display all method
	def display_all(self):
		print "Price: ${}, Speed: {}, Fuel: {}, Mileage: {}, Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

# Create six different instances of the car class
car1 = Car(2000, "35mph", "Full", "15mpg")

car2 = Car(2000, "5mph", "Not Full", "105mpg")

car3 = Car(2000, "15mph", "Kind of Fulll", "95mpg")

car4 = Car(2000, "25mph", "Fulll", "25mpg")

car5 = Car(2000, "45mph", "Empty", "25mpg")

car6 = Car(200000000, "35mph", "Empty", "15mpg")


