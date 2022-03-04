#Without return type
'''def fun1():
    print("Parent function")
    def fun2():
        print("This is child class")
fun1()'''

#Function with return type
def fun1():
    print("Parent function")

    def fun2():
        print("This is child function")
        return 'This is gani', fun2()
    return 'This is sai'

#    res2 = fun2()
#    print(res2)
res1 = fun1()
print(res1)


# Function with return type
def fun_one(str):
    return 'This is python1'

    def fun_two():
        return 'This is python2', fun_two()

#    res2 = fun2()
#    print(res2)
res2 = fun_one("Sai")
print(res2)

