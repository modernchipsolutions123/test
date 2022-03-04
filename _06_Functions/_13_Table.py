# Python Program to Print Multiplication Table of a Number
#1.Take input from the user
num = int(input("Enter the number: "))
#2.Multiplication of a given number
print("Multiplication Table of", num)
#3.Given range of a number
for i in range(1, 11):
    #4.Multiply of a number
   print(num,"X",i,"=",num * i)

num = int(input("Enter the number: "))
print("Multiplication Table of", num)
def table(num):
    for i in range(1, 11):
       print(num,"X",i,"=",num * i)
t1 = table(num)
print(t1)
