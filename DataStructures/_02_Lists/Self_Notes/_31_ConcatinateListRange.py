#35.Creating a list by cocatinating a given list which range goes from 1 to n
'''test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
for i in test_list2:
    test_list1.append(i)

# Printing concatenated list
print("Concatenated list using naive method : "
      + str(test_list1))
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,2]
for i in l1:
    l2.append(i)
print(str(l2))'''
my_list = ['k', 's', 'g']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

list1 = ['k','S','g']
n = 4
for x in list1:
    for y in range(1,n+1):
        print(x,y)