'''y= {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #Remove the dublicate elements from y
print("1:",x)
z = x.symmetric_difference(y) #Remove the dublicate elements from both x,y
print("2:",z)


x = {"apple", "banana", "cherry"}'''

def fun(y):
	y[0]=y[1]
	y[1]=y[0]
	print(y)
y=[10,20]
fun(y)


