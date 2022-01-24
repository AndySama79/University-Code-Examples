class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insert(self, item): #enqueue
        self.items.insert(0,item)

    def remove(self): #dequeue
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self): #return element at the head
        return self.items[len(self.items)-1]

q = Queue()
q.insert('a')
print(q.size())
q.insert('b')
print(q.size())
print(q.peek())

