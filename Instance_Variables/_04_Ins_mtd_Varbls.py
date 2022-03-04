'''
## wys tomcreate Instance Variables:
    1.By using constructor : Constructor used to initialize the instance variables
    2.By using instance method : A method which has self keyword
    3.By using object reference variable
'''
class Ins_Var_mtd:
    #1.By using constructor
    def __init__(self):
        self.name = "Kumar143"
        #2.By using instance method
    def display(self):
        self.partner = "Koushalya"
Ivm = Ins_Var_mtd()
Ivm.display()
#Object reference variable
Ivm.address = 'Chitoor'
print(Ivm.name,Ivm.partner,Ivm.address)