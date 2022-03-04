'''
NUMBERS :
        1. int  ---> 1,2,3...-1,-2,-3...
        2. float ---> 2.5,3.6 to -2.3,-5,8
        3. complex --> ai+2j,..
OPERATORS : OPeration between two operends
    Ex : a + b

 1. Arithmetic Operator ---> + , - , * , / , //


'''
# 1.1 Integer :
a = 10
b = 20
print(a+b)
x,y,z = 10,20,30
print(x+y+z)
print('................')
#1.2 Float
a ,b = 20.8 ,29.2
print(a+b)
#Arithmetic operator using float and  integer
a ,b = 20.5 , 3
print(a+b)
#Arithmetic operator using String and int and float
a = "Sai"
b = " Ganesh"
print("Using string :", a+b) #In string we concatinate


x = "Sai"
y = 20
#Can only concatinate string (not "int") to string
#print("Using string and int :" ,x+y)

#FLOATING :
a ,b = 2.5 , 3.6
print(a+b)
#List : List is a data type with  comma separated square brackets[1,2,4.5] wit different data types
#  Ex: l1 = [1,2.3,'sai']
l1 = [1,2,3.5]
l2 = [1,2,4.5]
print("Using list :", l1 + l2) #By using list we concatinate
l1 = [1,2,3]
t1  = (3.4,8.9)
#print("Using list and tuple :",l1 + t1)
#OUTPUT : can only concatenate list (not "tuple") to list
t1 = ("Sai","Has","a Pan")
t2 = [1,3,4.5]
#print(t1 + t2)
n = input("Enter the value :")
count = 0
for i in n:
    print(i)
    #count = count + i.count(int[0] + int[1])
    #print(count)



a = 56

print(type(a))

