#Python will give first preference to local variable
a = 10 #Global
def outer(): #Enclosing function
    b = 5 #Enclosing variable and Non-local
    def inner(): #Nested function
        c = 6 #local to the inner func
        nonlocal b
        b = b + 1 #We can't modify without using non-local keyword
        print("local to the inner func:",c)
        print("Global any where:",a)
        print("Encloser variable :",b)
    inner()
    print("Non-local:",b)
outer()