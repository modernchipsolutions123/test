#*args use to pass no of arguments to a function
#Variable length  :Multiple- arguments at a time. We don't no how many arguments to pass
'''
1.Function take input(arguments)
2.Variable - different length
3.When we don't know the length of arguments while defining fun,we use variable argument func
'''
def variable_args(*a):
    print(a)
    return
variable_args(10) #It will print as tuple

#Elements by using array
def variable_args(*arr):
    print("Elements are:")
    for ele in arr:
        print(ele)
    return
variable_args(10)

def fun1(*mylist):
    for num in mylist:
        print(num)
    return
fun1(10,20,30,40)
fun1(2.1,20.6,3.9)
fun1("Sai","Dhana","Jaya")
fun1(1,2,3,4,5)


def add(farg,*args):
    print('Formal argument=',farg)

    sum = 0
    for i in args:
        sum+=i #sum =sum + i
    print('Sum of all numbers =',(farg+sum))
add(5,10)
add(5,10,20,30)
