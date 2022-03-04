s1 = {1,2,4,6,8,12,145,16,18}
newset = set()
for ele in s1:
    if ele%2 == 0:
        newset.add(ele)
print("Original set s1: ",s1)
print("after dividing all elements by 2 newset: ",newset)

#Using list comprehension
mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = {element for element in mySet if element % 2 == 0}
print("The existing set is:")
print(mySet)
print("The Newly Created set is:")
print(newSet)
