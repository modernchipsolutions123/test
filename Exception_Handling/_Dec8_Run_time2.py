try:
    a = int(input("Enter 1st nbr :"))
    b = int(input("Enter 2nd nbr: "))
    print(a/b)
except:
    print("Except block is used to rectify errors from try block")
finally:
    print("finaly block will execute everytime ,it will not depands any Errors ")