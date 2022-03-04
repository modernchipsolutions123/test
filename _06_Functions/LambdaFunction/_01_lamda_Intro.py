
#1.A lambda function is a small anonymous function.

#2.A lambda function can take any number of arguments, but can only have one expression.


x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a:a+10
# Here we are printing the function object
print(x)   # It will print object address
print("sum = ",x(20))



