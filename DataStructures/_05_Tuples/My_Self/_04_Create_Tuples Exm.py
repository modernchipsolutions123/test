'''TUPLE : Exactly same as list Except that is Immutable,We can't change
		1.Read only version of list is python
		t = () #Tuple
		2.Comma separated values t =(10,)
		3. In tuple we can't use append and Extend ---> Arttribute error
		4.In tuple we cause different data types
'''

# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ",Tuple1)

# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("Tuple with the use of String: ",Tuple1)

# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
#Converting string to tuple
t1 = ('Ganesh')
print(tuple(t1))
#Create tuple using Built-in function
t2 = tuple("Kadali")
print(type(t2))