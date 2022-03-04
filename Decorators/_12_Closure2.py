#2.Functions are first class object
'''
CLOSURES : Closures is a function object that remembers values in the enclosing scope even if they are not present in
            memory
            1.Nested function
            2.Nested function must refer values in enclosing scope
            3.Enclosing function must return nested function
ADVANTAGES :
    1.Can avoid global values
    2.Data hiding
    3.Let us impliment decoraters
'''
def outer():
    x = 4
    def inner():
        y = 10
        res1 = x + y
        return res1
    return inner

a = outer()
print(a) # reference of an object Inner function 'a' is noting but inner function
print(a.__name__) #reference of a class name
print(a()) #a()enclosing function must return nested function



