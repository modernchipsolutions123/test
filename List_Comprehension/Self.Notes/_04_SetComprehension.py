s1 = {s for s in [1, 2, 1, 0]}
print(s1) #set([0, 1, 2]) -->Set will remove the dublicate elements
#Square of a set
s2 = {s**2 for s in [1,1,2,3,4,5,5]}
print(s2)
s3 = {a**3 for a in range(11)}
print(s3)

squares = []
for i in range(1, 11):
    squares.append(i**2)

squares_lc = [i**2 for i in range(1, 11)]