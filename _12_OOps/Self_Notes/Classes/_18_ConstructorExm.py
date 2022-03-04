# We can call constructor by explicitly,Then it will be executed like a normal method & new object won't be created
'''class Test1:
    def __init__(self):
       print("This is constructor")

# Creating object
t = Test1()
# Calling method Explicity
t.__init__()
t.__init__()
t.__init__()'''

# Constructor/Method Overloading concept  not possible
class Test1:
    # If we are trying to declare multiple constructor PVM will always consider only last constructor
    def __init__(self):
       print("No args in constructor")

    def __init__(self,x):
       print("One argument in Constructor")

# Creating object
t = Test1()
t = Test1(10)




