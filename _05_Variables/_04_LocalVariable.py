'''
Local Variable: A variable which is inside the function only and call only inside .We can't acess it anywhere
'''
def f():
    # local variable
    s = "I love Geeksforgeeks"
    print(s)
f()


def add():
    # Defining local variables. They has scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)
# Calling a function
add()