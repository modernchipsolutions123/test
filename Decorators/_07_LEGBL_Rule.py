'''
#Pytho first preference will give the local variable
LEGB-Rule : Local,Global,Encloser,Built-in
Local     : Contains names defined inside the current function
Global    : Contains names defined at the top level of the script or module
Enclosed  : Contains names built-in to the python language
Built-in  : Contains names built-i to the python language
'''
y = 20 #Global : Top level and outside the function ,we can call both inside and outside th function
def inner():
    x = 10 #Local :Inside the current function ,we can call only inside
    global y
    y = y+1 #we can't acess local variable with global variable by using global keyword we can acess
    print("Local Inside the function:",x)
    print("Global: inside:",y)

inner()
print("Global Outside :",y)

