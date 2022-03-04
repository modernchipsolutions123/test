try:
    def increment(sal):
        sal = sal * 15/100
        return sal
    sal = increment(5000)
    print("Increment salary :",sal)
except:
    print("Error occured in try block")

