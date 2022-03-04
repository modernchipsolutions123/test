class Ins_VarMtd:
     def __init__(self,name,age): #1. This method is used to instance variables
         self.name=name
         self.age=age       #1.1  Instance Variables

    #2.Instance Method
     def msg(self):
        print(self.name,self.age)

print("........OBJECT-1(p1)......")
p1=Ins_VarMtd("Ramya", 25)
print("Name:",p1.name)
print("age :",p1.age)
p1.msg()

print(".....OBJECT-2(p2).....")
p2=Ins_VarMtd("Sravani", 24)
print(p2.name)
print(p2.age)
p2.msg()