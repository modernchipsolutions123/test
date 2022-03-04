#2.Multi-levelInheritance :Grandparent class inherits  parentclass and parentclass inherit the child class (One_to_another)

class grand_parent:
    def msg(self):
        print("Kadali is grand Parent")

class parent(grand_parent):
    def display(self):
        print("sai is parent")

class child(parent):
    def get(self):
        print("ganesh is child")

c = child()
c.msg()
c.display()
c.get()