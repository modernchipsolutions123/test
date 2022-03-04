class Staticmtd:

    #1.STATIC METHOD : Without using Instance variable and class/static variable we use additional data
    @staticmethod
    def add(x,y):
        print("The Sum is :", x + y)

a1 = Staticmtd()
#By using reference variable to call the static method
a1.add(10,30)
#By usinf classname to call the static method
Staticmtd.add(4,5)