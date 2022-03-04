#By using Try Except
#Try : Try block will execute when the try block is true
#Except: Exception block is used to rectify Errors will execute when the try block occured Error()
'''try:
    a = int(input("Enter 1st nbr :"))
    b = int(input("Enter 2nd nbr: "))
    #print(a/b)
except:
    print("An Error occurd")'''

try:
    a = int(input("Enter 1st nbr :"))
    b = int(input("Enter 2nd nbr: "))
    print(a/b)
except:
    print("Except block is used to rectify errors from try block")

'''a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))

except:
    print("An error occurred")'''
