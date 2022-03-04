
class Name():
    def __init__(self,a , b , c ):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        print(self.a , self.b , self.c)
#By using default keywords only we use Overloading
n1 = Name(a=20,b=30,c=50)
n1.display()
n2 = Name(c=2,a=3,b=1)
n2.display()
n3 = Name(b=20*2,c=2.3+3-2,a=10/2-1.5)
n3.display()


