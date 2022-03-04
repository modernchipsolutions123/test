t = set()
print(type(t))
set1 = set(["Peter","Joseph", 65,59,96])
set2  = set(["Peter",1,2,"Joseph"])
#Union : It will combine both set1 set2
set3 = set1.union(set2)
print(set3)
print(type(set1))
#Intersection : It will print only common elements
set3 = set1.intersection(set2)
print(set3)

issubset = set1 >= set2
print(issubset)
issuperset = set1 <= set2
print(issuperset)
issubset = set3 <= set2
print(issubset)
issuperset = set2 >= set3
print(issuperset)
