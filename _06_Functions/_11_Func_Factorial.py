#4.Factorial of a given number
n = int(input("ENter the number:"))
res = 1
for i in range(n,0,-1):
    res = res*i
print("factorial of",n,"is",res)
#OUTPUT:
'''
range(5,0,-1)    i = 5,4,3,2,1
res = res * i 
 i =5
res = 1*5 = 5
 i =4
res =  5*4 =20
 i = 3
 res = 20*3 =60
 i = 2
res = 60*2 = 120
'''
'''
#BY using inbuilt method
#importing math module
import math
n1 = int(input("Enter the number:"))
res1 = math.factorial(n1)
print("factorial of",n1,"is",res1)'''


