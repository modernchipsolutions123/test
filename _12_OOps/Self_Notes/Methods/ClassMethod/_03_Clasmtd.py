class Clasmtd:
    #1.CLASS VARIABLE/STATIC VARIABLE : Inside the class and outside the method
    temple = "Paddintlama"
    village = "Mulalanka"

    #2.Class method is used to call the class or static variable and
    #2.1 we use Decorator@ ans cls as an claas method of reference
    @classmethod
    def msg(cls):
        #By using classname we call the class 0r static variable
        print(Clasmtd.temple)
        #By using class method  variable
        print(cls.village)

c1 = Clasmtd()
c1.msg()
