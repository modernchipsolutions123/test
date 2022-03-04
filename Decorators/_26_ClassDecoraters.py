class check_div:
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs): #args will give list of elements
        list1 = []
        list1 = args[1:]
        for i in list1:
            if args[1] == 0:
                return "You can't divide change the input!!"
                # print("You can't divide change the input!!")
            else:
                return self.func(*args, **kwargs)
@check_div
def div1(a,b):
    return a/b
@check_div
def div2(a,b,c):
    return a/b/c
print(div1(10,2))
print(div2(10,5,2))