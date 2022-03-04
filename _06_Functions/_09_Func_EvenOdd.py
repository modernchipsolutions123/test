#2.Print given number is even or odd
#Prime numbers : 2,3,5,7,11,13,17,19,23,29,31,37,41,47,53,59,61,67
#1.Take input from the user
nbr = int(input("Enter the number:"))
#2.Check the number is  even or odd.
if nbr%2==0:
    #if given nbr is even it will print even
    print("Given nbr is even")
else:
    #if given nbr is odd it will print odd
    print("Given nbr is odd")

'''#2.Using functions
nbr1 = int(input("Enter the number:"))
#Function deffination
def even_odd(nbr1):
    if nbr1%2==0:
        #2
        print("{0} is Even number".format(nbr1))
    else:

        print("{0} is odd number".format(nbr1))
#Function call
even_odd(nbr1)'''
'''
#Print even numbers and odd numbers 0 to 100
for nbr in range(0,100):
    print(nbr)
    if nbr%2==0:
        #if given nbr is even it will print even
        print("Given nbr is even")
    else:
        #if given nbr is odd it will print odd
        print("Given nbr is odd")'''
