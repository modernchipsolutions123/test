'''str1 = "Welcome to my python world \nWelcome to my python world"
print(str1)'''
'''
str1='Modernize chip solutions\npoornima is a python developer'
print(str1)
print(str1.rstrip())

def removelines(value):
    return value.rstrip()
mystring = 'This is my string. \n'
print("Actual string:",mystring)
print("After deleting the new line:",removelines(mystring))'''

str = "sai\n""ganesh\n""kadali"
print("Before remove new line of str: ",str)
s = str.split()
print("After split:",s)
print("Remove the new line:")
for i in s:
    print(i,end=" ")

