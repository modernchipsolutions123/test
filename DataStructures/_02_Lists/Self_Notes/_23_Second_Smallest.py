#27.Finding second smallest number
#METHOD 1:
l1 = [1,2,45,32,41,0,4,6]
print("Original list:",l1)
l1.sort()
print(l1)
print("Second smallest ",l1[1])
def find_len(list1):
    length = len(list1)
    list1.sort()
    print(list1)
    print("Second smallest element is:", list1[length - 2])

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print("Original of list1:",list1)
Largest = find_len(list1)

#METHOD 2 :
l2 = [1,4,6,0,66,99,88,55]
new_list = set(l2)
print(new_list)
new_list.remove(min(l2))
print("Second smallest :",min(new_list))
