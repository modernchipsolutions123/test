# mytuple=(i for i in range(1,11))
# print(mytuple) #It will print generator object
# for j in mytuple:
#     print(j)

'''
def harsha():
    name = 'harsha'
    return name

a = harsha()
print(a)
'''

def fib(myMax):
    a,b = 0,1
    while True:
        c = a+b
        if c < myMax:
            print("Before Yield Keyword")
            yield c
            print("After Yield Keyword")
            a=b
            b=c

        else:
            break
gen1 = fib(10)
print(gen1)
print(gen1.__next__())
print(gen1.__next__())




