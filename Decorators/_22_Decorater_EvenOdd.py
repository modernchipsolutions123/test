def dec1(func):
    def inner():
        res = func()
        if res%2==0:
            return f"Given nbr is even"
        else:
            return res
    return inner
@dec1
def even_odd():
    return 16
print(even_odd())
