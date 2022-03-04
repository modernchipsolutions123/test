from array import *
arr2 = array('f',[2.9,3,4,6.3,4.8,1,-1])
arr2.append(22.5)
arr2.pop()
print(arr2)
#arr3 = array(arr2.typecode,(a for a in arr2)) #typecode is used to copy the arr1 to arr2 at same datatype
#for i in arr3:
#    print(i)
#SQUARE
'''arr3 = array(arr2.typecode,(a*a for a in arr2))
for i in arr3:
    print(i)'''
arr3 =array(arr2.typecode,(a**2 for a in arr2))
for i in arr3:
    print(i)

