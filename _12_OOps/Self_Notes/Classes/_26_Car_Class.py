#Crate class with different types
'''

class Car:
    #State
    def __init__(self,modelName,Year):  #1.Parameterized Constructor
        self.modelName = modelName
        self.Year = Year
        #Behaviour
    def display(self):
        print(self.modelName,self.Year)
c1 = Car("KIA",2021)
c1.display()


class Car:
    def __init__(self,modelName,Year):
        self.modelName = modelName
        self.Year = Year
    def display(self):
        print(self.modelName,self.Year)
#Create nof of objects to the class
c1 = Car("KIA",2021)
c1.display()
c2 = Car("JAGWAR",2021)
c2.display()
'''
class Car:
    def __init__(self): #Class using Constructor
        self.modelName = "Range Rover"
        self.Year = 1990

c1 = Car()
print(c1.modelName)
print(c1.Year)

