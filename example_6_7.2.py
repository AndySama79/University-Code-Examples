class Parent():
	def __init__(self):
		self.c = 21
		self._d = 42 # d is protected instance variable 

	def get_d(self):
		return self._d

class Child(Parent):
	def __init__(self):
		self.e = 84
		Parent.__init__(self)
		self._d = 44

	def get_d(self):
		return self._d # should work


object2 = Parent()
print(object2.get_d())
# print(object2.d) # error as d is a protected instance variable

object1 = Child()
print(object1.get_d())
# print(object1.d) # error as d is a protected instance variable