class Add:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 50
    def diplay(self):
        print(self.a + self.b)

class Name:
    def __init__(self):
        self.a = "Kadali"
        self.b = " Sai"
        self.c = " Ganesh"
    def display(self):
        print(self.a + self.b + self.c)
n1 = Name()
#n2 = Add()
n1.display()