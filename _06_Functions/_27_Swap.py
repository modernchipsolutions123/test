'''a = int(input("Enter the value of x: "))
b = int(input("Enter the value of y:"))
temp = a
a = b
b = temp
print("After swapping : ")
print("Enter the value of x : ",a)
print("Enter the value of y : ",b)'''

def swap(a,b):
    print("BEFORE SWAPPING : ")
    print("Enter the value of x : ",a)
    print("Enter the value of y : ",b)
    temp = a
    a = b
    b = temp
    print("After swapping : ")
    print("Enter the value of x : ", a)
    print("Enter the value of y : ", b)
swap(10,20)
