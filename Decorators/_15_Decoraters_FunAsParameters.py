def str_title(fun): #fun --> is an function reference
    def inner():
        s2 = fun()  #calling that function with an object
        return s2.title() #by returning change the title
    return inner
@str_title #@decorator function name
def print_str():
    return "dhanunjaya"
print(print_str())