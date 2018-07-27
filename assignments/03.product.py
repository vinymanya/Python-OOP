# Product class
class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "For sale"

	# Every method that doesn't have to return something should return self.
	# sell method
	def sell(self):
		self.status = "Sold"
		return self

	def add_tax(self, tax):
		price_after_tax = self.price * self.tax
		return price_after_tax

	def return_item(self, reason):
		if self.reason == "defective":
			self.status = "Defective Product"
			self.price = 0
		if self.reason == "packed":
			self.status = "For sale"
		if self.reason == "unpacked":
			self.status = "used"
			discounted_price = self.price/0.2
			self.price = discounted_price
		return self

	# Display product information
	def display_info(self):
		print "Price: ${}, Item Name: {}, Weight: {}, Brand: {}, Status: {}".format(self.price, self.item_name, self.weight, self.brand, self.status)
		return self

# Create instances of Product class
product1 = Product(230, "Samsung J6", "200g", "Samsung")
product2 = Product(5, "ketchup", "120g", "Aniston")
product3 = Product(25, "fan", "2kg", "Sky")
product4 = Product(15, "cooking oil", "10kg", "kismet")
# Chaining methods
product1.display_info()
# product1.sell().return_item("defective").add_tax(0.5).display_info()













