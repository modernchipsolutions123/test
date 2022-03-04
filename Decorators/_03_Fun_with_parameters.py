def divide(x,y):
    print(x/y)
def outer_div(func):
    def inner(x,y):
        return func(x, y)
    return inner
divide1 = outer_div(divide)
divide1(4,2) 


