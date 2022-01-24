class Parent():
	def __init__(self):
		self.c = 21
		self.__d = 42 # d is private instance variable 

	def get_d(self):
		return self.__d

	# def set_d(self, d):
	# 	self.__d = d
	# 	return self.__d 

class Child(Parent):
	def __init__(self):
		self.e = 84
		Parent.__init__(self)

	def get_d(self):
		return self.__d #error when called

object2 = Parent()
print(object2.get_d())
# print(object2.__d) # error as d is private instance variable
object2._Parent__d = 400
print('Accessing successfully', object2._Parent__d)

object1 = Child() 
# print(object1.get_d()) # error as d is private instance variable
# print(object1.d) # error as d is private instance variable