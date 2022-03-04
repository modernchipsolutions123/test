#SINGLE DECORATER WITH MULTIPLE FUNCTIONS :
def div_decorater(func):
    def inner(*args):
        list1 = []
        list1 = args[1:]
        for i in list1:
            if i ==0:
                return"Give proper input!!!"
        return func(*args)
    return inner
@div_decorater
def div1(a,b):
    return a/b
@div_decorater
def div2(a,b,c):
    return a/b/c
print(div1(5,0))
print(div2(10,2,5))
