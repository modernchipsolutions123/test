# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ",Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Python', 2: 'T', 3: 'Point'})
print("\nCreate Dictionary by using  dict(): ",Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Devansh'), (2, 'Sharma')])
print("\nDictionary with each item as a pair: ",Dict)

# Creating a Dictionary
Dict = {1: 'Sai', 2: 'ganesh', 3: 'Kadali'}
# Deleting a key
# using pop() method
pop_ele = Dict.pop(3)
print("It will remove the key (3) value:",Dict)
