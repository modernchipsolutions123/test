#Decorater with parameters
def outer(expr):
    def msg_d(func):
        def inner():
            return func()+expr
        return inner()
    return msg_d
@outer(" Dhanunjaya") #Parameter to the decorater function
def ordinary():
    return "Indian kabadi player"
print(ordinary)



'''
def outer1(exp1):
    def dispaly_d(func1):
        def inner2():
            return func1()+exp1
        return inner2()
    return dispaly_d
@outer1(" Sudharshan")
def msg1():
    return "Good knowledge in python"
print(msg1())'''

#What is decorater
#Purpose of decorater.Adv and dis adv
#python decoraters
#Django Decor
#Fast API