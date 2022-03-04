from functools import reduce
l1 = [1,1,1,1,2,2,2,3,3,3]
a = []
b = []
c = []
for i in l1:
    if i == 1:
        a.append(i)
    elif i == 2:
        b.append(i)
    elif i == 3:
        c.append(i)
res1 = reduce((lambda x,y:x*y),a)
res2 = reduce((lambda x,y:x*y),b)
res3 = reduce((lambda x,y:x*y),c)
print(res1+res2+res3)