
# Math Dojo class
class MathDojo(object):
	def __init__(self):
		self.result = 0

	# Add method
	def add(self, *args):
		for num in args:
			if type(num) == list or type(num) == tuple:
				for i in num:
					self.result += i
			else:
				self.result += num
		return self

	# Substract Method
	def substract(self, *args):
		for num in args:
			if type(num) == list or type(num) == tuple:
				for i in num:
					self.result -= i
			else:
				self.result -= num
		return self


# Create a new instance of MathDojo
md = MathDojo().add(2).add(2,5).substract(3,2).result
print md

#Part Two:

# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. 
# It should now be able to perform the following tasks:
md2 = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).substract(2, [2,3], [1.1, 2.3]).result
print md2