#1.Using Functions
#STATE
#Class variables : Inside the class out side the method
std_id = 10
std_name = "K.S.G"
std_sal = 70000
#BEHAVIOUR
def display(std_id,std_name,std_sal):
    print("Student details:","ID",std_id,"NAME:",std_name,"SALARY:",std_sal)
display(std_id,std_name,std_sal)
#2.Using Class
class Student:
    #State
    #Class variables :A variable which is Inside the class outside the method.
    std_id = 10
    std_name = "K.S.G"
    std_sal = 70000
    #Constructor :It is used to inititalize the instance variables by using self keyword
    def __init__(self):
        #Instance variables
        self.a = 10
        self.b = 20
    #BEHAVIOUR
    #Method :Method is same as function.A method which is inside the class is called method outside class is function
    #Instance method :A method which has a self keyword
    def display(self):
        print("Class Variables :", "ID:", Student.std_id, "NAME:", Student.std_name, "SALARY:", Student.std_sal)
        print("Instance variables:",self.a,self.b)
    #Class method :By using class name only we can call the class method
    @classmethod
    def msg(cls):
        print("This is class method")
S2 = Student()
S2.display()
#Classmethod
Student.msg()
#print("It will print the address of s2 object:",S2)
#Calling class variable by using class name
#print(Student.std_id,Student.std_name,Student.std_sal)
