'''
CLOSURE : it has two types
 1.Nested function
 2.Functions are first class objects

'''
#1.Nested function
def outer():
    x = 4
    def inner():
        print(x)
    inner()
outer()

#2.Functions are objects
