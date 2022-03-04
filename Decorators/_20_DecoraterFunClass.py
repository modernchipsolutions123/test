def check_name(method):
    def inner(name_ref):
        if name_ref.name=='sai':
            print("My name is also same!!!")
        else:
            method(name_ref)
    return inner

class printing:
    def __init__(self,name):
        self.name = name
    @check_name
    def print_name(self):
        print("Enter user name is :",self.name)
p = printing("Kadali")
p.print_name()