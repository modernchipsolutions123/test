import copy
l1 = [[1,3,5],[2,4,6]]
l2 =copy.deepcopy(l1)
l1[1][1] = 50
print("coping to  l1",l1)
print("coping to g l2",l2)
