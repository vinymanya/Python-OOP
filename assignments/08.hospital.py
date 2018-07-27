class Patient(object):
	def __init__(self, _id, name, allergies, bed_number="none"):
		self._id = _id
		self.name = name
		self.allergies = allergies
		self.bed_number = bed_number


patient1 = Patient(1, "Hugg", "Flu", 5)

class Hospital(Patient):
	def __init__(self, hospital_name, capacity, _id, name, allergies, bed_number):
		super(Hospital, self).__init__(_id, name, allergies, bed_number)
		self.patients = []
		self.hospital_name = hospital_name
		self.capacity = capacity

	# Display hospital info
	def info(self):
		print "Hospital Name: {}, Number of patients: {}, Capacity: {}".format(self.hospital_name, len(self.patients), self.capacity)
		return self

	def admit(self, *args):
		self.patients.append(args)
		if len(self.patients) >= self.capacity:
			print "The hospital is full!"
		else:
			print "Ongoing admission!"
		return self

	def discharge(self, index):
	 	for i in range(0, len(self.patients)-1):
	 		if i == index:
	 			self.patients.pop(i)
	 			self.bed_number = "none"
	 	return self


hospital1 = Hospital("Medical-host", 2, 1, "John", "flu", 10)
hospital1.admit("Medical-host", 2, 1, "John", "flu", 10).info()

hospital2 = Hospital("Medical-host", 2, 2, "Owen", "diabetes", 2)
hospital2.admit("Medical-host", 2, 2, "Owen", "diabetes", 2).discharge(0).info()

