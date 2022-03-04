
#By using multiple list it will not change the both lists.It will change only one given list name'''

import copy
l1 = [1,2,3]
l2 = copy.deepcopy(l1)
print("Before adding l1:",l1)
print("coping to g l2:",l1)

l2[1]=40
print("after adding l1:",l1)
print("coping to g l2 it will not change:",l2)







