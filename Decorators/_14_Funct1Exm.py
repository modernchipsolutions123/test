#Storingthe function reference in a name and calling that
def str_upper(func):
    def inner():
       s1 = func()
       return s1.upper()
#    return inner() # With paranthesis
    return inner # Without paranthesis
def print_str():
    return "welcome to python"
p = str_upper(print_str)
#print(p) Without paranthesis for return inner to call
print(p()) #it will give reference of an object
print(print_str())