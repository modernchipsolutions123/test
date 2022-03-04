# Double all numbers using map and lambda
#MAP(function,iterable(Sequence,list,tuple set)) :
# function : function is used to Required. The function to execute for each item
#iterable : Required. A sequence, collection or an iterator object. You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

numbers = (2, 4, 6, 8)
result = map(lambda x: x + x, numbers)
print(result)
print(set(result))

n = (1, 2, 3, 4)
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
#n = (1, 2, 3, 4)
result = map(addition, n)
print(tuple(result))

# Add two lists using map and lambda
num1 = [1, 2, 3]
num2 = [4, 5, 6]
result = map(lambda x, y: x + y, num1, num2)
#print(result)
print(list(result))
#IT will find the length of the string
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(tuple(x))

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(tuple(x))