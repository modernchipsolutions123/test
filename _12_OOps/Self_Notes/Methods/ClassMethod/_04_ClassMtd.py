class ClsMtd:
    #Class Variable
    c = 40
    #Fields : State
    #Constructor: It is used to intialize  the instance variables
    def __init__(self):
       #Instance Variables :By using self
        self.a = 10
        self.b = 20
       #Behaviour
        #Instance Method :
    def display(self):
        print(self.a + self.b)
    @classmethod
    def msg(cls):
        print("This is class method")
        print("By usig ClassMethod :",cls.c)
c1 = ClsMtd()
c1.display()
c1.msg()
print("By using ClassName :",ClsMtd.c)
print("By using Reference of class object", c1.c)