'''
Global Vraible : A variable can use both inside and outside the class/function and print any where,By using increment inside
		the function use global keyword

'''
# This function uses global variable s
def f():
    print("Inside Function", s)
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)


x = 101
# Global variable in function
def mainFunction():
    # printing a global variable
    global x
    print(x)
    # modifying a global variable
    x = 'Welcome To Javatpoint'
    print(x)


mainFunction()
print(x)