'''
CLASS : It acts as blueprint/plan/model/design for objects
    *Every Class has (State) Variables and Methods (Behaviour)
    *3 types of Variables: Instance(OBJECT),Static(CLASS),Local(METHOD)
    *3 types of methods : Instance,Class,Static
#PVM :Python Virtual Machine provided self

OBJECT :A physical existance of a class,or an Instance of a class
    * We can create any number of objects (One-to-many)
'''
class Student:
    def __init__(self): # Default Constructor
        print("This is Constructor")
        self.name = 'Sravani'
        self.rollno = 143
        self.marks = 100

    def talk(self): # Method --> Behaviour
        print("Hello i am:",self.name)
        print("My rollno is:",self.rollno)
        print("My marks are:",self.marks)

# Where ever you are creating object automatically constructor will be execute
# Without constructor we can't create object in python
s = Student() #s is reference variable or object
#For every object creation automatically constructor will be executed
'''print(s.name)
print(s.rollno)
print(s.marks)'''
s.talk()
#REFERENCE VARIABLE : The variable which can be used to refer object
    # By using this reference variable we operate object i.e by using reference variable we can access Variables&Methods

