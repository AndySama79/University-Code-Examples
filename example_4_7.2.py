class Parent():
	def __init__(self):
		self.c = 21
		self.__d = 42

	def set_d(self, d):
		if d > 0:
			self.__d = d
		else:
			self.__d = 0

	def get_d(self):
		return self.__d

object1 = Parent()
print(object1.get_d()) 
object1.set_d(-43)
print(object1.get_d()) 