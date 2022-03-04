#Class : Class is a blue print or templete
#Class has STATE is Fields and BEHAVIOUR is Methods

    #STATE
        #Fields
        #1.Class variable :It can share and use any where
        #2.Instance variable : Data is unique
    #BEHAVIOUR
        #METHODS :A function which is inside the class
        #1.Class method
        #2.Instance method
        #3.Static method
class A:
    #1.STATE
    #Class Variable: A variable which is inside the class and outside the method.it can print anywhere
                    #By using class name we call class variables


    name = "Sai Ganesh Kadali"
    id = 10
    college = "G.V.P College"
    print("With out using class name directly print class variable name:",name)
    #BEHAVIOUR
    #Instance method :(self) By using self we call as instance method .
    def display(self): #Self -->Instance-Object-reference variable
        print(self.name,self.id,self.college)
        print(A.name)
a = A()
a.display()
print(a.id)
print(a.college)






