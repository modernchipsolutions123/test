#1.Sum of elements in list
l1 = [1,2,3,4,5,6]
#1.In_Built method sum()
print("1.adding all the elements in list by using sum() method:",sum(l1))

l1 = [1,2,4,6,8,10]
total = sum(l1) #Using sum() function
print("2.Sum of all eelments:",total)
#2.adding all the elements in list1 by using for loop
'''
1.Create a list
2.Iterate each element in list
3.adding all the elements in variable total
4.
'''
total = 0
list1 = [10,30,20,40]
for i in range(0,len(list1)):
    total = total + list1[i]
    print("Iterate one by one all the elements in list1 and add:",total)
print("3.Sum of all the elements in list1",total)