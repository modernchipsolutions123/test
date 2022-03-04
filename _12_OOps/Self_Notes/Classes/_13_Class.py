'''class A:
    pass
    def display(self):
        print("This if instance method")
a1 = A()
a1.display()
class Sum:
    #Class Variables
    a = 10
    b = 20
    print(a+b)
s1 = Sum()'''
class Add():
    #STATE
    #1.Default Constructor:It is used to initialize the instance variables
    def __init__(self):
        #Instance Variables
        self.a  = 10
        self.b = 20
        self.c = 30
    #BEHAVIOUR
    def display(self):
        print(self.a + self.b + self.c)
a2 = Add()
a2.display()


class car:
    #2.Parameterized constructor
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(self.modelname, self.year)


c1 = car("Toyota", 2016)
c1.display()