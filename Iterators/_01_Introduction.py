'''
ITERATORS : Iterator is an object that contains countable no.of values
    * By using this object we can traverse through all the values
    * In python,iterator is an object it impliments iterator protocol

#It consists of the methods
    1.__iter__()
    2.__next__()
#Iterator objects :
1.Lists
2.Tuple
3.Sets
4.Dictionary
'''
# define a list
my_list = [4, 7, 0, 3]
# get an iterator using iter()
my_iter = iter(my_list)
#print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
