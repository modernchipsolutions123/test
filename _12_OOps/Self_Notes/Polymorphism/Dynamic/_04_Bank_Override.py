#MULTI-LEVEL Inheritance : (One to One) ChildClass(ICICI) inherits sBI and SBI inherits Bank
class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    #Override : same method name with different classes
    def getroi(self):
        return 7
class ICICI(Bank):
    def getroi(self):
        return 8
i = ICICI()
print("It will print ICICI bank rate interest: ",i.getroi())
i1 = SBI()
print("It will print SBI rate interest :",i1.getroi())
i2 = Bank()
print("It will print Bank interest :",i2.getroi())



