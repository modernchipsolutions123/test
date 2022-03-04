#MULTIPLE DECORATERS ---> USING SINGLE FUNCTION
#Decorater : A decorater in python any callable object that is used to modify a function or a class
'''def msg1_d(func):
    def inner1():

        return "first "+func() +" first"
    return inner1
def msg2_d(func):
    def inner2():
        return "second "+func() +" second"
    return inner2
@msg2_d
@msg1_d
def display():
    return "Welcome to python"
print(display())'''
def upper_d(func): #Encloser  func --> is an function reference
    def inner1(): #Nested function -->used for modify function as weel as return that
        res1 = func()
        return res1.upper() #Changing into upper case letter
    return inner1 #Return the function
def split_d(func): #Encloser
    def inner2(): #Nested function
        res2 = func()
        return res2.split() #Changing into upper case letter
    return inner2 #Return the function
@split_d #Create decoraters
@upper_d
def ordinarry():
    return "dhanunjaya is a python developer"
print(ordinarry())


