
'''class Test:
    def __init__(self):
        print("Constructor")
    def m1(self,x):
        print('Method')
t1 = Test()
t1.m1(10)'''



class Student:
    def __init__(self,name,rollno,marks): #Parameterized Constructor
        print("This is Constructor")
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self): # Method --> Behaviour
        print("Hello i am:",self.name)
        print("My rollno is:",self.rollno)
        print("My marks are:",self.marks)
s1 = Student('Ramya',1,96) #s1 is reference variable or object
print(s1.name,s1.rollno,s1.talk())
s1.talk()
s2 = Student('Sravani',2,90)
s2.talk()
