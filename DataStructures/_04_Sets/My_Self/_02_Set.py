s = {1,2,3,4}
t = {1,7,2,4,6,9}
#Intersection : Print only commom elements
print(s.intersection(t))
print("Printing commom elements of s and t :",s & t)
print("Printing commom elements of s and t :",s.issubset(t))
#Union : Print bot s and t elements into one set
print("It will print both:",s.union(t))
#difference (s-t),(t-s) :
print("Printing except common elelements of s: ",s.difference(t))
print("Printing except common elements of t :", t.difference(s))
#s^t : It will print all elements except common elements in both
print("Printing all the elements except common elements in both s , t ",s ^ t)
#Issubset : It will give true when all elements of s are in t sets otherwise false
print(s.issubset(t))
#Issuperset : It will give true when all elements of t are in s sets otherwise false
print(s.issuperset(t))
print("It will print in a assending order:",sorted(t))



