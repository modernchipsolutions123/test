class InVr:

    #Constructor
    def __init__(self,a,b):
        #1.INSTANCE VARIABLES
        self.a = a
        self.b = b     #1.1 Directly we are initializing the instance variables b = 10
        self.c = a * b


      #2. INSTANCE METHOD
    def display(self):

         print("Division  c = :", self.a / self.b )
print("Object....1:")
biv = InVr(6,29)
biv.display()
print("Object...2:")
biv2 = InVr(2,4)
biv2.display()