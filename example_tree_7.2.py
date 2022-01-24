class Tree:
	def __init__(self, data):
		self.children = []
		self.data = data

	def add_child(self, child):
		self.children.append(child)

	def traverse(self):
		print(self.data) # 1 2 5 3 4
		if len(self.children) == 0: 
			return
		else:
			for child in self.children: #t -> [c1, c2, c3] c1 -> [c4]
				child.traverse()


t =  Tree('1')
c1 =  Tree('2')
c2 =  Tree('3')
c3 =  Tree('4')
c4 =  Tree('5')

t.add_child(c1) # t -> c1
t.add_child(c2) # t -> c1, c2
t.add_child(c3) # t -> c1, c2, c3
c1.add_child(c4) # t -> c1, c2, c3, c1 -> c4

#    t
# c1 c2 c3
# c4

t.traverse()