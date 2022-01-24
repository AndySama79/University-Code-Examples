class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item): #push
        self.items.append(item)

    def remove(self): #pop
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self): #return element at the head
        return self.items[len(self.items)-1]


s = Stack()
s.insert('a')
print(s.size())
s.insert('b')
print(s.size())
print(s.peek())



