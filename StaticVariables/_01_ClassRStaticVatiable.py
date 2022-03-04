'''
#Static or Class Variable : A variable which is inside the class and outside the method
    *Within a class dirctly we initialize the variable
    *By using class name we crate static variable in constructor
    *By using class name we crate static variable in method

'''
class Test:
    x = 20  #Static variable
    def __init__(self):
        Test.y = 30 #Static variable by using classname
        self.z =40
        print("This is Constructor")
    def display(self):
        Test.a = 50
        print("This is Method")
t1 = Test()
t1.display()
print("Z value: ",t1.z)
print(Test.x)
print(Test.y)
print(Test.a)
