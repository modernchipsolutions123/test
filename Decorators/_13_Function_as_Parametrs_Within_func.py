#Function as parameter within function
def function1():
    print("Hi i am function1")
def function2(func):
    print("Hi i am function2 now i call function1")
    func()
function2(function1)
