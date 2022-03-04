#1.Create function
def display(str):
#2.Inside function
    def message():
        #2.1 Return inside function
        return 'How aere you'
    #2.2 Call the inside function
    res1 = message() + str
#1.1. return out side function
    return res1
#1.2 Call the function
print(display("Sai"))

#Functions can be passed as parameters to other functions
def display1(fun):
    return 'Hai' + fun
def message1():
    return 'How are u? '
#d = display1()
#print(d)
#m = message1()
#print(m)
#Call display1() function and pass message() function
print(display1(message1()))
