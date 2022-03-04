#1.Create list
list = [10,30,8]
#Create a function from list
def maximum(list):
    #Return max number of a list
    return max(list)
#Call the function and passing values to the variable
m1 = maximum(list)
print(m1)

#1.Create a function
def max(a, b, c):
#2.Check the condition which number from a,b,c is maximum number
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest
'''a = 10
b = 14
c = 12'''
#print(max(a, b, c))
m1 = max(10,14,12)
print(m1)