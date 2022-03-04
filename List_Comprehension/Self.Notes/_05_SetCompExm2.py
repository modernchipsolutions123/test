s1 = {s for s in range(1,11) if s % 2}
print(s1)
#set([1, 3])
#Nested for loop by using list comprehension0
s2 = {(a,b) for b in range(2) for a in range(3,6)}
print(s2) #It will print the pairs
