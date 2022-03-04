#Child class Inherits the all the methods and properties of both Grandfather and Father classes
#Grand Father
class Calculation1:
    def Sum(self,a,b):
        return a+b;
#Father
class Calculation2:
    #This method is override
    def Sub(self,a,b):
        return a-b;
    def Mul(self,a,b):
        return a*b;
#Child
class Derived(Calculation1,Calculation2):
    def Div(self,a,b):
        return a/b;
d = Derived()
print("Adding a and b:",d.Sum(10,20))
print("Multiplication of a and b:",d.Mul(10,20))
print("Dividing the elements a  and b:",d.Div(10,20))
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))