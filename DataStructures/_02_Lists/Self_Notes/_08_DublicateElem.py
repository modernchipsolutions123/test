'''#7.Remove dublicate elements of list
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

list1 = [1,2,2,4,6,6,9]
list1 = list(dict.fromkeys(list1))
print(list1)

# removing duplicated from list
# using list comprehension

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]
# printing list after removal
print("The list after removing duplicates : " + str(res))

list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(list))
# to remove duplicated
# from list
res = []
for x in list:

    if x not in res:
        res.append(x)
#        print()
# printing list after removal
print("The list after removing duplicates : " + str(res))'''
#1.Initializing list
l1 = [1,2,3,4,5,1,2,6,7,9]
print("Original list:",l1)
res = []
for x in l1:
    if x not in res:
        res.append(x)
print("After removing dublicate values:",res)

