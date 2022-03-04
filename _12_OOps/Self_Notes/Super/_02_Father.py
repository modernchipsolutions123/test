class Father:
    def __init__(self ):
        self.name = 'Sai'
        self.age = 20
    def display(self):
        print('This is SuperClass', self.name , self.age)
class Son(Father):
    def __init__(self, name , age ):
        self.name = name
        self.age = age
    def display(self):
        print("This is BaseClass", self.name , self.age)
    #Super() : It is used to call the super class method
        super().__init__()

s = Son('gani',22)
s1 = Son('kadali',123)
s.display()
s1.display
