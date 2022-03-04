'''#SELF: Self is used to object itself
    Self is used to differentiate b/w Instance and Local variables
    Instance Variable : the variable belongs to an object
    Local Variable :
                        '''
class mtd:
    #2.METHOD : A function which is inside class is called method
    def __init__(self,name): #3.This __init__ method is used to initialize the variables
        #4.self.name is an Instance variable
        self.name = name  #4.name is an local variab3le
    def display(self):
        a=10
        print(a)
    def display2(self):
        print("A function which is inside the class is called method")
m=mtd()
m.display()
m.display2()