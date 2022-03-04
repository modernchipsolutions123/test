'''#Super() method is an built-in method,
Deffination :
super() function returns a temporary object of parentclass
and is used to allow acess to all of its method to its childclass'''

#PARENT CLASS
class Parent:
    def __init__(self, name):
        print('Parent__init__', name)

#CHILD CLASS
class Child(Parent):
    def __init__(self):
        print('Child__init__')
        #This super function is used to return the temporary object of parent class and call the parent class
        super().__init__('max')

c = Child()
#c.__init__()

