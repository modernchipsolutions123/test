#create Empty set
s = set()
#2.Adding elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print("After adding all the elements to the sets",s)
for i in s:
    print("Iterating the set one by one:",i)
#REmove:
s.remove(4)
print(s)
t = {2,4,8,6}
print("It will print only common elements of s and t:",s & t)
print("It will combine all the elements from s and t",s.union(t))
