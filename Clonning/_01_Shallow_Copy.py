#Copy :The process of creating exactly duplicate object is called clonning R copy
'''ShallowCopy : If the original object contains any reference to mutable object,
                just dublicate reference variable will be created pointed to
                old contained objects,but not dublicate objects creation
'''
import copy
l1 = [10,20,[30,40],50]
print(id(l1[2]))
l2 = copy.copy(l1)
l1[2][0] = 666
print("l1:",l1)
print("l2:",l2)
print(id(l1))
print(id(l2))
print(id(l1[2]))
print(id(l2[2]))



