#Create tuple with mixed  data typ
Tuple1 = (5, 'Welcome', 7, 'Sai')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

# Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'Programming')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)\

# Creating a Tuple with repetition
Tuple1 = ('kadali',) * 3
print("Tuple with repetition: ")
print(Tuple1)

# Creating a Tuple with the use of loop
Tuple1 = ('Sarani')
n = 5
print("Tuple with a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)
