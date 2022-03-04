'''
1.First we have to import array module
2.We can store multiple values in a single variable with one data type

'''
from array import *
arr1 =array('i',[1,2,-2,3]) # i -->Both positive and negative values in an array
print("i take Both positive and negative values in an array",arr1)
print("Size and address of an array:",arr1.buffer_info())

arr1 =array('I',[1,2,22,3]) #I -->It will take only positive values
print("I will take only positive values",arr1)

arr1 =array('i',[122,-234,321,4321])
print(arr1)
#"It will print reverse of a given number by using reverse():"
arr1.reverse()
print("It will print reverse of a given number by using reverse():",arr1)
'''
arr2 =array('f',[12.2,-2.34,32.1,43.21])
print("f take Both positive and negative values in an array",arr2)

arr2 =array('F',[12.2,-2.34,32.1,43.21])
print("I will take only positive values",arr2)'''

#print size of an array(arr1), and address of an array(buffer_info())
print(arr1.buffer_info())

arr1.reverse()
print("It will print reverse of a given number by using reverse():",arr1)
#It will print index of an value
print(arr1[2])





