# Python Program to Calculate Cube of a Number
#1.Create a function with out parameters and with out return type
def cube():
#Given number as input from the user
    number = float(input(" Please Enter any numeric Value : "))
#find the cube of a given number
    cube = number ** 3

    print("The Cube of a Given Number {0}  = {1}".format(number, cube))
#Calling function
cube()

#2.Create a function with  parameters and with  return type
#2.1 Given number as input from the user
nbr1 = int(input(" Please Enter any numeric Value : "))
#2.2 Function with parameter
def cube(nbr1):
#2.3 Function with return type
    return nbr1 **3
#2.4 call the function and pass to the variable by using return type
c1 = cube(nbr1)
#Print cube of given number
print(c1)
#Square of a given number
n1 = int(input(" Please Enter any numeric Value : "))
def cube(n1):
    return n1 ** 2
sq1 = cube(n1)
print("Square of a given number:",sq1)

