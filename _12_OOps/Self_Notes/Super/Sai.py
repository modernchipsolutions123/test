class Sai1:
    def display(self):
        print("Parent1 Class")

class Sai2:
    def diaplay(self):
        print("This is Parent2 Class")
class Child(Sai2,Sai1):
    def display(self):
        print("This is child class")
        super().display()


c1 = Child()
c1.display()
print(Child.__mro__)
