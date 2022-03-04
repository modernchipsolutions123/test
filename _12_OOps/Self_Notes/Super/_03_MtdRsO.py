class Parent1:
    def __init__(self):
        print("Parent1 class __ini__ method")

class Parent2:
    def __init__(self):
        print("Parent2 class __ini__ method")


class  Child(Parent1,Parent2):
    def __init__(self):
        print("This is child Class __init__ method")
        #Super() fuction returns an temporary object of the superclass that allow acess to all of its method to its child class
        super().__init__()
        #Parent2().__init__()


c = Child()
#Method Resolution Order(MRO):it is used to print first all the methods of child class after parent class from Left to Roght
print(Child.__mro__)
