class Parent():
	def __init__(self):
		self.c = 21
		self.d = 42

	def set_d(self, d):
		if d > 0:
			self.d = d
		else:
			self.d = 0

object1 = Parent()
print(object1.d)
object1.d = -43 
print(object1.d)