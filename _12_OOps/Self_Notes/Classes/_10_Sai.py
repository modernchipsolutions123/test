'''
Class : Class is a blueprint (Design)or a template
Object : Instance of a class
'''
class Sai:
    #Constructor : It is used to initialize instance variables
    def __init__(self):     #SELF : defaultVariable contains memory address of instance os currentclass
        #Instance Variables3
        self.vlg = 'mlk'
        self.phn = 9256660666
    #Instance method
    def display(self):
        print("Village name is :", self.vlg)
        print("Pno is :",self.phn)
s = Sai()
s.display()



