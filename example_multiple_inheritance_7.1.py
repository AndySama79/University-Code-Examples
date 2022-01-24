class Parent1():
    def __init__(self):
        self.str1 = "P1"
        print("Parent1")
class Parent2():
    def __init__(self):
        self.str2 = "P2"        
        print("Parent2")
  
class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child")
    def printStrs(self):
        print(self.str1, self.str2)
        
ob = Child()
ob.printStrs()
