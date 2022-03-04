'''class Decorater:
    def __init__(self,func):
        self.func = func
    def __call__(self):
        str1 = self.func()
        return str1.upper()
@Decorater
def display():
    return "Welcome to python"
print(display())'''

class check_div:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs): #args will give list of elements
        if args[1]==0:
            return "You can't divide change the input!!"
            #print("You can't divide change the input!!")
        else:
            self.func(*args,**kwargs)

@check_div
def div1(a,b):
    return a/b

print( div1(10,0)) 