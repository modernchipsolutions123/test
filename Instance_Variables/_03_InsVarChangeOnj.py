class Ins_Var:
    def display(self):
        print("Welcome to instance variables")
s1 = Ins_Var()
s1.name = "Ramya"
s1.rollno = 222
s1.address = "Visakapatnam"
print(s1.__dict__)
