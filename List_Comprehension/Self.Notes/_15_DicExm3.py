#Without using dictionary comprehension
dictionary = dict()
for k1 in range(1,5):
    dictionary[k1] = dict()
    for k2 in range(6,9):
        dictionary[k1][k2] = k1*k2
print("Without using dictionary comprehension")
print(dictionary)

#Using dictionary comprehension
dictionary = dict()
for k1 in range(1, 6):
    dictionary[k1] = {k2: k1*k2 for k2 in range(1, 6)}
print("Using dictionary comprehension")
print(dictionary)


dt1 = dict()
dt2 = {k2:k1*k2 for k2 in range(1,6)}
print(dt2)


