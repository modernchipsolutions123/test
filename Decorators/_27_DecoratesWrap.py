import functools
def decorater(func):
    @functools.wraps(func) #It will copy the last data from the undecorater function or original func to decorater closer
    def inner():
        str1 = func()
        return str1.upper()
    return inner
@decorater
def greek(): #Original function
    return "Welcome to python"
#print("Function name calling: ",greek.__name__) #OP: inner, adding functionality it will hide data from original func
print("Function name calling: ",greek.__name__) #Hides some data from original function like(name,docstring,parameters)
print(greek())


