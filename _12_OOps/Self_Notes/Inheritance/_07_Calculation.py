class Calculation:
    def sum(self,a,b):
        return a + b

class Calculation2:
    def mul(self,a,b):
        return a * b
    #both parentclasses(Claculation, calculation2)class inherits childClass(DerivedClass):
class Derived(Calculation,Calculation2):
    def Divide(self,x,y):
        return x/y
d = Derived()
print(d.sum(10,5))
print(d.mul(2,4))
print(d.Divide(10,2))
