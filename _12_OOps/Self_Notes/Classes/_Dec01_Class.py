class A:
    #Class variable : A variable which is inside the class outside the the method
    #Class variable can print any where by using class name
    name = "Sai"
    Color = "Blue"
    def __init__(self,id,age):
        #Instance variable : By using self keyword
        self.id = id
        self.age = age
        print(A.name)

        #Instance method :
    def display(self):
        print(self.id,self.age)
        #print(A.name)


    def msg(cls):
        print("Class Method",A.name,A.Color)

a = A(143,24)
a.display()
#print(A.name)
a.msg()