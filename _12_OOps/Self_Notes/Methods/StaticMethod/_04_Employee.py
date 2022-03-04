class Employee:

    #1.STATE :

    #Fields : 1.Class Variables     : Inside class and outside method and It can share anywhere
    office='Modern Chip Solutions'

             # 2. Instance Variables  : By using self object we caal that instance variable
    def __init__(self):
        self.name = 'Ganesh'
        self.id = "2019"
        self.salary = "10,000"

    #2.BEHAVIOUR :

     #Methods : 3 types
    #1.Instace method: We use self object
    def msg(self):
        print("He was living in bangloure "+ "ID:",self.id  + " NAME:" + self.name  +" Salary: "+ self.salary)

    #2.Class method : We use only class variable by using class name or cls method and decorators(@)
    @classmethod
    def display(cls):
        print(cls.office)

    #3.Static method : Using additionaldata without using any instance&class method
    @staticmethod
    def get_salary():
        print("Hike my salary")

 #By creating object of a class we call the class
e1 = Employee()
e1.msg()
e1.display()
#By using class name and object reference we call the static method
e1.get_salary()
Employee.get_salary()



