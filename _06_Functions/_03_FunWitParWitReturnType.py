num1 = 100
num2 = 20
#Function with parameters with return type
def display(num1,num2):
    res = num1 + num2
    return res
op = display(num1,num2)
print("Addition is:",op)

a = 10
b = 20
def display(a,b):
    res = a + b
    return res
op1 = display(a,b)
print("Output of a func:",op1)

#By using operators
def disp2(a,b,c):
    res1 = a + b + c
    return res1
op2 = disp2(1+4,10-5,2*2+1)
print("By using operators:",op2)

def msg(x,y,z):
    c = x - y * z
    return c
op3 = msg(10,-15,5)
print(op3)

def fun(n1 , n2):
    #State
    n1 = int(input("Enter the 1st number:"))
    n2 = int(input("Enter the 2nd number:"))
    #Behabviour
    res = n1 + n2
    return res
a=fun()
print(a)

def fun1():
    #State
    num1 = input("Enter the 1st string:")
    num2 = input("Enter the 2nd string:")
    #Behaviour
    num = num1 + num2
    return num
f=fun1()
print(f)

def msg():
    #State
    a = input("Enter the string1:")
    b = input("Enter the string2:")
    #Behaviour
    c = a + b
    return c
m = msg()
print(m)




