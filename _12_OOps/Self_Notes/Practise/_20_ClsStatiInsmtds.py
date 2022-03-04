class ClsStatiInsmtds:

    #1.Class/Static variable
    Ins = "MCS"

    def __init__(self,name,branch,city):
        #2.Instance variables
        self.name = name
        self.branch = branch
        self.city = city

    #3.Instance method
    def msg(self):
        print(self.name +" "+ self.branch )

    #4.ClassMethod : It used to print the classvariable by using ClassName/cls
    @classmethod
    def display(cls):
        print(cls.Ins)

     #5.StaticMethod : It is used to print additional data without using InstanceVariables and ClassVariables
    @staticmethod
    def add(a,b):
        print("The smarks is :", a + b )

CS1 = ClsStatiInsmtds("Sravani", "CSE", "Kalidindi")
#3.1 It is used to print the instance of a method
CS1.msg()
#4.1 It is used to print the class method
CS1.display()
#5.1 It is used to print the static method
CS1.add(50,30)
CS2 = ClsStatiInsmtds("Ramya", "CSE", "Kalidindi")
CS2.msg()
CS2.display()

CS2.add(30,80-90+30)






