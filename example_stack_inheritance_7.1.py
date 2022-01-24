class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert_(self, item): #enqueue
        self.items.insert(0,item)

    def remove(self): #dequeue
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self): #return element at the head
        return self.items[len(self.items)-1]

class Stack(Queue):

     def insert_(self, item): #push
         self.items.append(item)

     def remove(self): #pop
         return self.items.pop()


# s = Stack()
# s.insert_('a')
# print(s.size())
# s.insert_('b')
# print(s.size())
# print(s.peek())

q = Queue()
print(q)
print(q.items)

l = ['a', 'b', 'c', 'd']

for i in l:
    q.insert_(i)
    print(q.items)

q.remove()
print('removed')
print(q.items)

s = Stack()
print(s)
print(s.items)

l = ['a', 'b', 'c', 'd']

for i in l:
    s.insert_(i)
    print(s.items)

s.remove()
print('removed')
print(s.items)