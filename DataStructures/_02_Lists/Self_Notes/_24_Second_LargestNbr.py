#28.Finding second Largest number
#METHOD 1:
l1 = [1,2,45,32,41,0,4,6]
print("Original list l1:",l1)
l1.sort()
print(l1)
print("Second largest ",l1[-2])
def find_len(list1):
    length = len(list1)
    list1.sort()
    print(list1)
    print("Second Largest element is:", list1[length - 2])

list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)

#METHOD 2 :
l2 = [1,4,6,0,66,99,88,55]
print("Original list l2 :",l2)
new_list = set(l2)
print(new_list)
new_list.remove(max(l2))
print(new_list)
print("Second largest l2:",max(new_list))

'''def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))'''
