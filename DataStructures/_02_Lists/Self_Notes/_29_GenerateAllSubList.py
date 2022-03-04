#33.Generate all sublist
# function to generate all the sub lists
'''def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
l1 = [1, 2, 3]
print(sub_lists(l1))'''

l1 = [1, 2, 3]
lists = [[]] # Empty sub list
for i in range(len(l1)):
    print("i value",i)
    for j in range(i):
        print('j value',j)
        lists.append(l1[j: i])
print(lists)
