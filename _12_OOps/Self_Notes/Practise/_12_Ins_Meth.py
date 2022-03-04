class Ins_Meth:
    # Class me3thod : Inside the class and out side the3 me3thos
    city = "Vizag"
    #1.CONSTRUCTOR : It is used to initialize the instance variables
    def __init__(self):
        self.college = "Gayathri"
        self.name = "Kadali"        #1.1 INSTANCE3 VARIABLES : directly we3 can assign the values to veriable
        self.id = 10
        self.fees = 61000

    #2..Instance Method : A method which is declare inside the class
    def display(self):  #2.1 SELF is used to object itself

        print("College_name :",self.college)
        print("Name :",self.name)
        print("Id :",self.id)
        print("Fees :",self.fees)
        #3.By using class name we can call the class variable
        print("City :",Ins_Meth.city)

I = Ins_Meth()
I.display()
#3print("City :", Ins_Meth.city)

