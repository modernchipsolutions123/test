#Membership Operator :in , not in :
'''# 1.in
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,1,2]
for i in l1:
    if i in l2:
        print(i)'''
#2. not in
l1 = [1,2,3,4,5,6]
l2 = [7,8,9,1,2]
for i in l1:
    if i not in l2:
        print(i)
    if i not in  l1:
        print(i)

for j in l2:
    if j not in l1:
        print(j)
    if j not in  l2:
        print(j)
