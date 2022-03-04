class Test:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

t1 = Test('Dhnanunjaya',143,90)
print(t1)

class Test1:
    def __init__(self):
        self.name = "Dhana"
        self.rollno = 123
        self.marks = 99

    def test_py(self):
        print(self.name,self.rollno,self.marks)

t1 = Test1()
t1.test_py()

class Test2:

     def display(self):
         print("This is method")
t2 = Test2()
t2.display()



