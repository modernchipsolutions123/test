'''
try:
    n = int(input("Enter the nbr:"))
    for n in range(1,n+1):
        print(n)
except:
    print("Error occured in try block")
'''
# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("true")
    else:
        print("False")
except:
    print("Not an even number!")
    reciprocal = 1/num
    print(reciprocal)


