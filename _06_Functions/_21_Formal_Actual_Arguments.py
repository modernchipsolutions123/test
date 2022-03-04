#a,b are formal arguments :A arguments inside the function deffination
#Function deffination
def sum(a , b):
    c = a + b
    print(c)
x = 50
y = 20
#Call the function
#x,y are actual arguments : A arguments inside the function call
sum(x,y) #

def sub(x,y): #Formal arguments
    z = x - y
    print(z)
a,b =20,30
sub(a,b) #Actual arguments

def avg(n1,n2,n3):
    return (n1+n2+n3)/3.0
print("Welcome")
num1 = int(input())
num2 = int(input())
num3 = int(input())

res = avg(num1,num2,num3)
print(res)