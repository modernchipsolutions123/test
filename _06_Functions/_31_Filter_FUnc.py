#Print even numbers by using filter()
f1 = filter(lambda x:x%2==0,range(1,11) )
print(f1)
#By using list
l1 = list(filter(lambda x:x%2==0,range(1,11) ))
print("By using list:",l1)
#BY using tuple
t1 = tuple(filter(lambda x:x%2==0,range(1,11) ))
print("By using tuple:",t1)
#By using set
s1 = set(filter(lambda x:x%2==0,range(1,11)))
print("By using set:",s1)

# Take a list of numbers.
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
# use anonymous function to filter and comparing
# if divisible or not
result = list(filter(lambda x: x % 13 == 0, my_list))
# printing the result
print(result)