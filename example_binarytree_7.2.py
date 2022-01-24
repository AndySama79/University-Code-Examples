class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	def add_child_right(self, child):
		if self.right is None: 
			self.right = child
		else:
			print('Overwriting', self.right.data, 'by', child.data)
			self.right = child

	def add_child_left(self, child):
		if self.left is None: 
			self.left = child
		else:
			print('Overwriting', self.left.data, 'by', child.data)
			self.left = child

	def traverse(self):
		print(self.data) # 1 3 2 4 5
		if self.left is not None:
			self.left.traverse()
		
		if self.right is not None:
			self.right.traverse()

		return None #implicit

t =  BinaryTree('1')
c1 =  BinaryTree('2')
c2 =  BinaryTree('3')
c3 =  BinaryTree('4')
c4 =  BinaryTree('5')

t.add_child_left(c2)
t.add_child_right(c1) 
c1.add_child_left(c3)
c1.add_child_right(c4)

# 1
#3  2
# 4   5

t.traverse()