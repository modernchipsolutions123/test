#23.Flatten a shallow : Combine all the elements in one list
'''import itertools
original_list = [[1,2,3],[4,5],[6],[7,8,9]]
new_mergeList = list(itertools.chain(*original_list))
print(new_mergeList)'''
'''
l1 = [[1,2,3],[4,8,10],[6],[5,7,9]]
for i in l1:
    for j in i:
        print(j,end='')'''
#By using functions
def shallow_Com(num):
    return [x for y in num for x in y]
num = [[2,4,6,8],[1,3,5,7],[22,66,33,99]]
print("Original list: ",num)
print("\nCombine the list: ")
print(shallow_Com(num))
