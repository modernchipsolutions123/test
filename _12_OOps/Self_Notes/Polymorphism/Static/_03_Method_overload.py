class Father_overload:

    def __init__(self,property=1000000,name='kadali',phno=9876543143):#Default Parameters
        # SELF : it is used to contain memoryaddress of instance of currentclass
        self.property = property
        self.name = name
        self.phno = phno
    #OVERLOADE :  By using default keywords we use overloading.Python does not support overloade
        print(self.property, self.name, self.phno)

print(".........Positional Arguments.........")
f = Father_overload(100000, "Sai")#Positional Arguments
print("..........Keyword Arguments..............")
f1 = Father_overload(name ="Gani",phno= 9876543213,property = 2000000,)#KeyWord Arguments
print("..........Default Arguments..............")
f2 = Father_overload()




