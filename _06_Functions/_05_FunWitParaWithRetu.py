#1.Function with parameters and with return type
def display(a,b,c):     #Function deffination with parameters
    z = a + b + c
    return z        #Return type
op1 = display(10,20,30)  #Function call same as function deffination
print(op1)

def dis1(n1,n2,n3):  #Function deffination with parameters
    n1 = input("Enter the String1:")
    n2 = input("Enter the String2:")
    n3 = input("Enter the String3:")
    return n1,n2,n3 #Return type
op2 = dis1(1,2,3)   #Function call same as function deffination
print(op2)

def message(a ="Python"):
    return a
op3 = message("gani")
print(op3)


