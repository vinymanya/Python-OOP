# store class

class Store(object):
	def __init__(self, location, owner):
		self.products = []
		self.location = location
		self.owner = owner

	def add_product(self, product):
		self.products.append(product)

	def remove_product(self, product):
		self.products.pop(product)

	def inventory(self):
		if self.products:
			for product in self.products:
				print "Product's Name: {}, Location: {}, Owner's Name: {}".format(product, self.location, self.owner)

store1 = Store("Cyprus", "viny")
store1.add_product("Cooking oil")
store1.inventory()
print store1.products


