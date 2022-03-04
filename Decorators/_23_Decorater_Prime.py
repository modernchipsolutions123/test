def dec1(func):
    def inner():
        res = func()
        c=0
        for i in range(1,res+1):
            if res%i==0:
                c +=1
        if c==2:
            return f"prime number"
        else:
            return f"not prime number"
    return inner
@dec1
def prime():
    return 5
print(prime())
