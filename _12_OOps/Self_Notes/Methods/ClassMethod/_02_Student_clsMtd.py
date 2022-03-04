class Student_clsMtd:

    #1.Init Method : It is used to initialize instance variables
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    #2.Instance Method :
    def msg(self):
        print(self.name  + " got marks :" + self.marks, "%")

    def get_per(cls,name,marks):
         return cls(name,  marks)




s1 = Student_clsMtd("sai",78)

name = "Gani"
marks = 550
m1 = str( int(marks) /600 )*100
s2 = Student_clsMtd(name,m1)
s2.msg()