'''class A:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

#METHOD : Without return type
    def my_func(self):
        print(self.fname,self.lname,self.age)
        print("This is method 1")

    def display(self):
        print("This is method 2")
a1 = A("Sai","Kadali",23)
a1.my_func()
a2 = A("Ganesh","Kadali",20)
a2.my_func()'''
'''class B:

    def my_j(self):
        a = 10
        b = 20
        c = a + b
        print(c)

a = B()
a.my_j()'''
class B:
    fname = "balu"
    name = "Rajesh"

    def my_j(self):
        print(self.fname,self.name)

a = B()
a.my_j()
