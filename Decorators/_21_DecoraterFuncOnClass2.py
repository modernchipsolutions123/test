
def check_nbr(method):
    def inner(var_ref):
        if var_ref==10:
            print("Value of A is 10")
        else:
            method(var_ref)
            #print("Value of B")
    return inner

class var:
    def __init__(self):
        self.a = 10
        self.b = 20
    @check_nbr
    def display(self):
        print("Value of A:",self.a,"\n""Value of B:",self.b)
v1 = var()
v1.display()