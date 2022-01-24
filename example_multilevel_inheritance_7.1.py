class Parent:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Child(Parent):
    def __init__(self, name, age):
        Parent.__init__(self, name)
        self.age = age
    def get_age(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
    def get_address(self):
        return self.address        

g = GrandChild("Sukrit", 29, "Plaksha")  
print(g.get_name(), g.get_age(), g.get_address())
print(g)
print(g.name)