class Employee:
    #Class Varaible : A variable which is inside the class Outside the method
    id = 10
    name = "Devansh"
    def display (self):
        #print(self.id,self.name)
        print(Employee.name)

E = Employee()
print(E.id)
E.display()
