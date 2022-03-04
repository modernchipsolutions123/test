print("********LIST In_Built functions********")
#Create empty list
list1 = []
list1.append([1,2,6])
print("Adding listof elements to list1 by using append:",list1)
list1.extend([10,20,7])
print("Extend by adding elements into the list :",list1)
list1.pop()
print("It will remove the last element:",list1)
list1.pop(2)
print("It will remove the given position element in list:",list1)
list1.remove(10)
print("Remove the goiven element of list",list1)

list1[0] = 200  #  Replace the value in index
print("After index   : ",list1)

list1.insert(0, 300) #  Insert the value in index
print("After insert  : ",list1)
list1.insert(5, 400)
print("After insert   : ",list1)
print("List index : ",list1.index(200))
# 8. reverse ==> list.reverse()  Reverses objects of list in place
list1 = [1,2,3,4,5]
list1.reverse()
print("List after reverse : ",list1)


print("")
#2.LIst can allow different data types
l1 = [1, 2.3, "Sai", True]
l2 = [20, 40, "Gani", 1, True, False]
print("Adding li1 and li2 is concatination:", l1 + l2)
print("Multiply li1 with 2 repetation is ", l1 * 2)
print("Length of the list li1 is:", len(l1))
l3 = [20, 90, 80, 30]
print("Maximum of list is ", max(l3))
print("Minimum of list is ", min(l3))
print("Slicing of list li3,reverse", l3[::-1])
print("Slicing in list:", l3[0:3])
print("Index values from list:", l3[1])
l4 = [1,3,5,6,9,2,4]
print("Sorting  assending order is:", l4.sort())

l4.sort(reverse = True)
print("Sortig in decending order:",l4.sort())

#Copy()
l5 = [2,4,8,6,10]
l6 = l5
print("copying l5 to l6",l6)
li3 =["Sai","Gani","Kadali"]
li4 = li3().copy()
print("Copying li1 to li2",li4)


