#Frcusion : A function calling itself
#Two cases;
#   1.BASE      : Terminating for recursion
#   2.RECURSIVE : Keep calling itself
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:                        #BASE Case
        return n*factorial(n-1)
n = int(input("Enter the value of n :"))
res = factorial(n)                          #RECURSIVE
print(res)
'''
res =factorial(5)
    5 * factorial(5-1) = 20
    20 * factorial(4-1) = 60
    60 * factorial(3-1) = 120
    120 * factorial(2-1) = 120
'''



