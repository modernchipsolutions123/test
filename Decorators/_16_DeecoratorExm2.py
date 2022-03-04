def div_decorater(func): #Encloser
    def inner(x,y):  #Nested function :  used for modify function as weel as return that
        if y == 0:
            return 'zero division error'
        return func()
    return inner

@div_decorater
def div(a,b):
    return a/b
print(div(5,0))

def mul_decorater(func):#Encloser  #func --> is an function reference
    def inner(a,b):
        if a == 10:
            return a*b
        return func()
    return inner #inner is a function
@mul_decorater
def mul(x,y):
    return x*y
print(mul(10,2))