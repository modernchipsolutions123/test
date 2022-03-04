class Bank:
    def getroi(self):
        return 10;
class SBI:
    def getroi(self):
        return 7;
class ICICI(Bank,SBI):
    def getroi(self):
        return 8;

b1 = Bank()
print("Bank Rate of interest:", b1.getroi());
print("SBI Rate of interest:", b1.getroi());
print("ICICI Rate of interest:", b1.getroi());
s1 = SBI()
print("Bank Rate of interest:", s1.getroi());
print("SBI Rate of interest:", s1.getroi());
print("ICICI Rate of interest:", s1.getroi());
c1 = ICICI()
print("Bank Rate of interest:", c1.getroi());
print("SBI Rate of interest:", c1.getroi());
print("ICICI Rate of interest:", c1.getroi());