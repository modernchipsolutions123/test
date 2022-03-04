#OVERRIDE :Run_time
class Father:
    #1.FIELDS :state --> vaiables , methods ,constructor
    #Constructor : It is used to initialize  instance variables by using self keyword
    def __init__(self):      #SELF : it is used to contain memoryaddress of instance of currentclass
        self.property = 8000000.00

    def display_property(self):
        print('Fathers Property =', self.property)

class Son(Father):
    pass    #PASS : We do not want to write anything in the subclass

#Create sub class instance and display fathers property
s = Son()
s.display_property()