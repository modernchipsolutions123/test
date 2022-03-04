'''
InstanceVariables:
    *By using one object to another object to change the values to use
    *By using constructor instance variable can be created by using self keyword.Every object has seperate copy
    *By using  instance method can be created by using self keyword
    *Outside of class using object reference
'''
class InstanceVar:
    #Constructor with out passsing any parameter
    def __init__(self):
        self.name = 'Kadali'
        self.rollno = 123
Ins = InstanceVar()
#print(Ins.name)
print(Ins.__dict__)

class Ins_Var:
    #Costructor by using parameters
    def __init__(self,n,r):
        self.name = n
        self.rollno = r
I1 = Ins_Var("Dhana",143)
I2 = Ins_Var("Sohel",1)
print(I1.__dict__)
print(I2.__dict__)

