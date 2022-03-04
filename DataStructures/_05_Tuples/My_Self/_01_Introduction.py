#Tuple : Tuple is immutable. It is enclosed with paranthesis (,) .And we can't change the values
#There was no  append,extend,insert
#It has multiple data types
#In tuple there was no append(),extend(),insert()
#Create tuple
t1 = ()
print(type(t1))
a = (1,2.4,"sai",100)
print(type(a))
#Update tuple : By using Concatination '+', we can't update one tuple to another
a = (1,2,3,4)
b = (5,6,7,)
c = a + b
print(c)
#Deletion : We can delete the tuple .but we can't delete elements of that tuple
#del a[1] #TypeError: 'tuple' object doesn't support item deletion
#print(a)
del a
#print(a)
#Accesing elements : By using slicing only we can acess tuple by using index
b = (1,2,4,6,8,9)
print("By using index (len-1):",b[0:4])
print("By using index (len-1):",b[3:])
print("By using index (len-1):",b[:5])
#length
print("Length of b:",len(b))
#OPERATIONS :
print("Length of b:",len(b))
c = (11,12,14,16)
#Conatination : By using + only we can update tuple
print("Update tuple",b+c)
#print(c+2) TypeError: can only concatenate tuple (not "int") to tuple
#Repeatation : Multiply uses only for repeting elements of tuple,We can't multiply b and c
print("Repeating tuple",b*2)
#Max : Maximum element of tuple
print("Maximum element of tuple is:",max(c))
#Min : Minimum element of tuple
print("Minimum element of tuple",min(c))
#Index : It will position of the element
print("Idnex position of the tuple",c[3])
b = (1,2,4,6,8,9)
c = (1,2,4,11,2,2,14,16)
#Membership : in,not in
print("check the tuple b elements is there in c or not given T or F: ",b in c)
print("check the tuple b elements is there not in c or not given T or F: ",b not in c)
#Count : count the elements of tuple
print("Count the no.of times repeated elements in tuple:",c.count(2))
tuple("Hello")
print("Conversion of tuple:",tuple)
#List into tuple:
list = [1,2,3,4]
print("Conversion of list into tuple",tuple(list))
#Iterative :
for i in c:
    #print("It will print onebyone:",c)
    print("It will iterate one by one in c:",i)







