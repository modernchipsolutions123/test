#CallMethod: CallMethod is an special method which will execute when we call the object in function
class Call_mtd:
    def __init__(self,name):
        self.name = name
    #CallMethod is special method
    def __call__(self):
        print("Enter user name :",self.name)
c1 = Call_mtd("Sai Ganesh")
c1()

class Call_mtd:
    def __init__(self):
        self.a = 10
        self.b = 30
    #CallMethod is special method
    def __call__(self):
        var1 = self.a + self.b
        return var1
c1 = Call_mtd()
print(c1())
'''class Decorater:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        str1 = self.upper()
@Decorater
def display():
    return "Welcome to python"
print(display())'''


