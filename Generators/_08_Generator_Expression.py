# Generator expression
list = [1,2,3,4,5,6]
a = (x ** 3 for x in list)

print(a)#Object reference
print(a.__next__())
print(a.__next__())
print(a.__next__())