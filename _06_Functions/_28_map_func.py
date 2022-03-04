#MAP(function,sequence) : sequence --> list, tuple ,set
#map function using lambda function

#String
a = input().split() #It will read each and every input in string format  i single line
print(a)
print(type(a))

a = list(input().split()) #It will read each and every input in string format  i single line
print(a)
print(type(a))

#Integer format by using map() function
b = list(map(int,input().split()))
print(b)
print(type(b))
#  List Floating format by using map()
b = list(map(float,input().split()))
print(b)
print(type(b))
#Tuple
#String
t = tuple(map(input().split()))
print(t)
print(type(t))
#Tuple integer
t = tuple(map(int,input().split()))
print(t)
print(type(t))
#Tuple Float
t = tuple(map(float,input().split()))
print(t)
print(type(t))
#set string
s = set(map(input().split()))
print(s)
#set integer
s = set(map(int,input().split()))
print(s)
#set float
s = set(map(float,input().split()))
print(s)

