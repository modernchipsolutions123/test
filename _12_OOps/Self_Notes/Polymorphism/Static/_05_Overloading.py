class Overlading:
    #Class Variable : Inside the class outside the method
    surname = 'kadali'
    #OVERLOADING : Both parent and child class having same method name at compile time
    def display(self):
        print("This is parent clas")
    def msg(self):
        print("This is parent method")

class Over(Overlading):
    def display(self):
        print("This is child class")
    def msg(self):
        print("This is child method", Over.surname)

o = Over()
o.display()
o.msg()
#print(o.surname)