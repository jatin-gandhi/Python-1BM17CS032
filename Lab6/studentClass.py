class student(object):
	def __init__(self,number):
		self.number=number
		self.name=None
		self.age=None
		self.marks=None
		self.usn=None
	def set(self):
		self.name,self.usn,self.age,self.marks = input("Enter NAME , USN ,AGE ,MARKS\n").split()
		self.age=int(self.age)
		self.marks=int(self.marks)
	def get(self):
		print("\nName : ",self.name ,"\nUSN: ",self.usn,"\nAge: ",self.age,"\nMarks: ",self.marks)
	def validate_age(self):
		if self.age>=20:
			return True
		return False
	def validate_marks(self):
		if self.marks >=0 and self.marks <=100:
			return True
		return False
	def check_qualification(self):
		if self.validate_age() and self.validate_marks():
			if self.marks >=65:
				return True
		return False


size = int(input("\nEnter the number of students\n"))
objects=[]
for i in range(size):
	objects.append(student(i))
for obj in objects:
	obj.get()
	obj.set()
for obj in objects:
	if obj.check_qualification():
		print("\n***********Qualified***************\n")
		obj.get()
	else:
		print("\n***********NOT Qualified***********\n")
