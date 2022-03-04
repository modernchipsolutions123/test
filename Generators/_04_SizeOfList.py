#Size of the list
'''def table1(n):
    list1 = []
    for i in range(1,21):
        list1.append(f'{n} X {i} = {n * 1}')
    return list1 #By using return size will increase
t2 = table1(4)
import sys
size = sys.getsizeof(t2)
print("Size:",size)
for i in t2:
    print(i)    #We can use multiple times in return function(Normal function)
for i in t2:
    print(i)'''

def table1(n):
    for i in range(1,21):
        yield f'{n} X {i} = {n * 1}'
t2 = table1(4)
import sys
size = sys.getsizeof(t2)
print("Size:",size)   #By using generator yield size will decrease
for i in t2:
    print(i)    #By using yield statement in generators we print only once
for i in t2:
    print(i)
#size(return)---> 10 lines 184 bits,20 lines 248
#size(Generator)--->Both 10&20 lines 112 bits .It is used to save memory
