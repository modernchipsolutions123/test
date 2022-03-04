#Sets:{,}
'''
1.Sets are similar to list and tuple.
2.It can't allow dublicate elements.
3.Set is also a collection of multiple elements of different data types
4.Set enclosed with curly braces {}
5.In sets there was no indexing and slicing
'''
#1.Create set with inbuilt metyhods
s = {1,2,3}
t = {4,5,6}
#1.Adding elements to set
s.add(7)
print("Adding the elements:",s)
#2.Update : Update one set to another
s.update(t)
print("Set 's' to 't' update in s:",s)
print("Length of the set:",len(s))
#Remove: it is used to remove given element of s and if it is not found give error key error
s.remove(5)
print("Remove the element in set :",s)
#Discord : it is used to remove given element of s and if it is not found give error key error
s.discard(7)
print("Discard remove element",s)
#Pop : It will remove first element of set
s.pop()
print("Remove the first element of set:",s)
#Clear: It will remove all the elements of set given empty set
s.clear()
print("Remove all the elements of set:",s)
s1 = {1,2,3,9,8}
print("Original set",s1)
#Max : It will give maximum element of s
print("Given maximum element of set s:",max(s1))
#Min : Given the minimum value of set s
#min(s1)
print("Minimum value of set:",min(s1))
#Sum : it will all elements of a set sum(s1)
print("Sum of all the elements in set:", sum(s1))




