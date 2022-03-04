class ClsMtd:
    # 0.Class Variable
    count = 0

    # Constructor
    def __init__(self, a, b):
        # 1.INSTANCE VARIABLES :By using self object we call that variables
        self.a = a
        self.b = a  # 1.1 Directly we are initializing the instance variables b = 10
        self.c = a - b
        # 0.1 By using  class variable we use the class name as an obj to increment the count
        ClsMtd.count = ClsMtd.count + 1

    # 2. INSTANCE METHOD : BY using self object we using that variables
    def display(self):
        print("Subbraction c = :", self.a - self.b)

    #3.By using classmethod we have to change the class
    @classmethod
    def obj_count(cls):
        return cls.count


print("Object....1:")
Cl1 = ClsMtd(6, 29)
#Cl1.display()
print("Object...2:")
Cl2 = ClsMtd(2, 4)
#Cl2.display()
print("Object...3:")
Cl3 = ClsMtd(10, 5)
#Cl3.display()
#4.By using classname or Obj also we have to call the class method and it will print no.of objects is created
#4.1 By using class name
print("No.of objects is created :",ClsMtd.obj_count())
#4.2 By using Class object
print(Cl3.count())