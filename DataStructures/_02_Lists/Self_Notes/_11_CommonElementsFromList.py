#11.Find common elements from two lists
l1 = [1,2,4,6,8]
l2 = [2,4,5,6,7]
a = set(l1)
b = set(l2)
l3 = [value for value in l1 if value in l2]
print(a&b)

# Python program to find the common elements
# in two lists
#1.Create two lists
a = [2,4,6,8,10]
b = [2,3,4,5,6]
#2.Converting list to set
a_set = set(a)
b_set = set(b)
#3.Check the list have common elements or not
if (a_set & b_set):
    print(a_set & b_set)
else:
    print("No common elements")

print(a_set & b_set)



