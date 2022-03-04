class Student:
    # Class Variable
    clg="Gayathri"
    #1.__init__ method is used to intiallize the attributes
    def __init__(self, id, year, name,branch,phno):
        # 1.STATE
        #1.1 Self is used to instance variables
        self.id = id #Fields
        self.year = year
        self.name=name
        self.branch=branch
        self.phno=phno

        # 2.BEHAVIOUR
    def display(self):   #Methods
        print("Student Details...")
        print("College_Name :",Student.clg, "Student_id : ",self.id,"PassedOut :", self.year,
               "Student_name :",self.name, "Branch_Name :",self.branch,
              "Phno :",self.phno)


s = Student(1, 2019, "Kadali", 'MCA', 9848780087)
s.display()
s1=Student(2, 2019, "Sai", "MCA", 9484740074)   # 2.s,s1,s2 is an object of a class
s1.display()
s2=Student(3, 2019, "Ganesh", 'MCA', 9666066066)
s2.display()

