'''class Student:
    #Class variables : A variable which is inside the class outside the method.Class variable can call anywhere
    college = "G.V.P College"
    #CONSTRUCTOR :Two types
    #1.Default Constructor
    def __init__(self):     #init method is used to initialize the instance variables by using self
        self.name = "Kadali"
        self.phno = 123456789
        self.branch = "M.C.A"

    def mtd(self):
        print(self.name,self.phno,self.branch)
s1 = Student()
s1.mtd()'''

class Sai:
    #2.Constructor Parameterized
    def __init__(self,a,b,c):
        self.a = 10
        self.b = 20
        self.c = self.a + self.b

    def disp(self):
        print(self.a + self.b )
S2 = Sai()
S2.disp()
