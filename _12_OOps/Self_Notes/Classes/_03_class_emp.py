class Employee:
    #1.__init__ method is used to intiallize the attributes
    def __init__(self, id, year, name,branch):
        # 1.STATE
        #1.1 Self is used to instance variables
        self.id = id #Fields
        self.year = year
        self.name=name
        self.branch=branch

        # 2.BEHAVIOUR
    def display(self):   #Methods
        print("Student Details...")
        print(self.id, self.year, self.name, self.branch)


e = Employee(1, 2019, "Kadali", 'MCA') # 2.s1 is an object of a class car
e1=Employee(2, 2019, "Sai", "MCA")
e2=Employee(3,2019, "Ganesh", 'MCA')
e.display()
e1.display()
e2.display()

