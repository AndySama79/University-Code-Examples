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
		print(self.data)
		if self.left is not None:
			self.left.traverse()
		
		if self.right is not None:
			self.right.traverse()

class MaxHeap(BinaryTree):
	def __init__(self, data):
		BinaryTree.__init__(self, data)

	def add_child_right(self, child):
		if child.data <= self.data:
			BinaryTree.add_child_right(self, child)
		else:
			print('Cannot add child because', child.data, '>', self.data)

	def add_child_left(self, child):
		if child.data <= self.data:
			BinaryTree.add_child_left(self, child)
		else:
			print('Cannot add child because', child.data, '>', self.data)

t =  MaxHeap(1)
c1 =  MaxHeap(2)
c2 =  MaxHeap(3)
c3 =  MaxHeap(4)
c4 =  MaxHeap(5)

t.add_child_right(c1)
t.add_child_left(c2)
c1.add_child_left(c3)
c1.add_child_left(c4)

t.traverse()


# t =  MaxHeap(5)
# c1 =  MaxHeap(4)
# c2 =  MaxHeap(3)
# c3 =  MaxHeap(2)
# c4 =  MaxHeap(1)

# t.add_child_right(c1)
# t.add_child_left(c2)
# c1.add_child_left(c3)
# c1.add_child_left(c4)

# t.traverse()