class Student:
    #1.Class Variable : A variable which is inside class Outside the method
    CollegeName = 'G.V.P'
    director = 'Ramya'
    #Constructor :It is used to initialize the instance variables
    def __init__(self,name,rollno):
        #Instance variable : A  value of variable is varied from object to object
        self.name = name
        self.rollno = rollno
    #Instance Method
    def getStudentInfo(self):
        print("Student Name :",self.name)
        print("Student Rollno :",self.rollno)

    #Class Method :
    @classmethod
    def getCollegeInfo(cls):
        print("College Name :",cls.CollegeName)
        print("Director Name :",cls.director)

    @staticmethod
    def getAverage(a,b,c):
        return (a+b+c)/3
s = Student("SRS",1995)
# Calling Instance variable
s.getStudentInfo() #Calling Instance variable
#Calling ClassMethod
Student.getCollegeInfo()
#Static method
avg = Student.getAverage(10,20,30)
print("Average :",avg)
