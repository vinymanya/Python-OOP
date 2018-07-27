import md5
#  Call class

class Call(object):
	def __init__(self, unique_id, name, phone_number, time, reason):
		self._id = md5.new(unique_id).hexdigest() 
		self.name = name
		self.phone_number = phone_number
		self.time = time
		self.reason = reason
	# Dsiplay call info
	def display(self):
		print "ID: {}, Name: {}, Phone Number: {}, Time: {}, Reason: {}".format(self._id, self.name, self.phone_number,self.time, self.reason)

# Create a new instance
call1 = Call("12345", "Teggy", "12-111-2-3", "12:30", "info")
call1.display()


# call center class
class CallCenter(Call):
	"""docstring for CallCenter"""
	def __init__(self, unique_id, name, phone_number, time, reason):
		super(CallCenter, self).__init__(unique_id, name, phone_number, time, reason)
		self.calls = []
		self.queue_size = len(self.calls)

	# Add method
	def add(self, *args):
		for i in args:
			if type(i) == list or type(i) == object:
				for k in i:
					self.calls.append(k)
			else:
				self.calls.append(i)
		return self

   #  def remove(self,*args):
   #  	for i in args:
			# if type(i) == list or type(i) == object:
			# 	for k in i:
			# 		self.calls.pop(k)
			# else:
			# 	self.calls.pop(0)
   #      return self

	# Info method
	def info(self):
		print "Name: {}, Phone Number: {}, Queue Size: {}".format(self.name, self.phone_number, self.queue_size)
		return self

#  Test cases
calling = CallCenter("2345", "Guy", "1222222222", "10:00", "news about the service")

calling.add(call1).info()



