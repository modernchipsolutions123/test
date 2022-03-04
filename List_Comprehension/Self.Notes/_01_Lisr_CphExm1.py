'''#Without list comprehension
letters = []
for letter in 'Python':
    letters.append(letter)
print(letters)'''

#Using list comprehension
#Syntax : newlist = [expression for item in iterable if condition == True]

l1 = [l1 * 2 for l1 in "K.s.g"]
print(l1)
l2 = [l2 * 2 for l2 in range(1,11)]
print("Range of func l2 : ",l2)
#list by using string
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#String by using upper method
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if x != "apple"]
print("Changing to upper : ",newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ["Kadali" for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#By using list
l2 = [1,2,3,4,5,1.9,3.5,66]
a = [i for i in l2 if i==4]
print(a)

l3 = [12,14,1,6,18,9]
b = [l3 if l3!=10 else 11 for i in l3]
print(".....",b)

#By using range
nl = [a for a in range(11)]
print(nl)

nl = [a for a in range(11) if a < 8]
print(nl)
