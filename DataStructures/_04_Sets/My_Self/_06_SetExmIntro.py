'''
SET :{}
1.Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
2.Set items are unchangeable, but you can remove items and add new items.
'''
set1 = {"apple", "banana", "cherry", "apple"}
print(set1)
#Get the Length of a Set
print(len(set1))

#The set() Constructor
set2 = set(("apple", "banana", "cherry"))
print(set2)
# Note: the set list is unordered, so the result will display the items in a random order.
#Adding elements to list
set2.add("orange")
print(set2)
#Update : Adding elements to list
tropical = {"pineapple", "mango", "papaya"}
set2.update(tropical)
print(set2)
#Remove : Remove the elements of list,If the item to remove does not exist, remove() will raise an error.
set2.remove("banana")
print(set2)
#Discard : Remove the elements of list,,If the item to remove does not exist, remove() will not raise an error.
set2.discard("banana")
print(set2)
x = set2.pop()

print(x) #removed item

print(set2) #the set after removal


