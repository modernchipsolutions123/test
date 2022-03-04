#reduce(): This reduce() function will reduce iterable to single element using some functions.
#1The output from reduce function is single element
#2.By using module functiontools we can reduce function and print o.p in a single element

import functools
num = [1,2,3,4]
r1 =functools.reduce(lambda x,y:x+y,num)
print(r1)
n1 = (2,4,6,8)
#r2 = functools.reduce(lambda a,b:a+b,n1)
print(functools.reduce(lambda a,b:a+b,n1))
#print(r2)

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["Kadali ", "Sai ", "ganesh"]))