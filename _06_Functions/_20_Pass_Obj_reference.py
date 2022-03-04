def modify(x):
    'Reassign value to a variable'
    x = 15
    print("Local variable of x :",x ,"Address of x: ", id(x))
x = 10
modify(x)
print("Global variable of x :",x ,"Address of x:", id(x))

#create a list
lst = [2,4,6,8]
#Passing list to a function
def mod1(lst):
    print("Before addind element to list:",lst)
    "Add a new element to list"
    lst.append(9)
    print("After adding element to list:",lst, "Adress of list:",id(lst))

#Call mod1() and pass lst
#lst = [2,4,6,8]
mod1(lst)
print("After adding element to list:", lst, "Adress of list:", id(lst))

def display(lst):
    lst = [10,12,14]
    print(lst , id(lst))
lst = [2,4,6,8]
display(lst)
print(lst,id(lst))
