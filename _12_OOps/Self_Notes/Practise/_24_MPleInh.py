class parent:
    def display(self):
        print("This is parent class")

class child:
    def msg(self):
        print("This is child class")

class daughter:
    def get_dis(self):
        print("This is daughter class")
class grandPaa(parent,child,daughter):
    def get_dau(self):
        print("All parent,child,daughter classes are inherit to grandparentclass")

gp1 = grandPaa()
gp1.display()
gp1.msg()
gp1.get_dis()
gp1.get_dau()



