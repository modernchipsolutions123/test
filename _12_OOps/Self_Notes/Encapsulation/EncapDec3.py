dic1 = {'k1':1,'K2':2,'K3':3}
class Sai:
    def __init__(self):
        self.k1 = 1
    def display(self):
        print(self.k1)

class Gani(Sai):
    def __int__(self):
        self.K2 = 2
    def msg(self):
        print(self.K2)
g1 = Gani()
g1.display()
g1.msg()
