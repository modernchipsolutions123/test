#INHERITANCE : Accquering properties and behaviours of one class to another class and IS_A relationship

'''
1.Single Inheritance : Childclass inherits the parentclass/Derivedclass inherits the Baseclass
'''
    #PARENT CLASS
class Iherit:
     def display(self):
         print("Parent class")

    #CHILD CLASS
class chid(Iherit):
    def msg(self):
        print("Child class")

    def display(self):
        print("Welcome to python")

#1.By using parent class name object it will print only parentclass methods
i1 = Iherit()
i1.display()
#i1.msg() it will not print because it is an child class
#2.By using child class name object it will print both parent and childclass methods
i2 = chid()
i2.display()
i2.msg()



